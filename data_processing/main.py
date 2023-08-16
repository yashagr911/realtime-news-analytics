from azure.eventhub import EventHubConsumerClient
from sentiment_analysis import analyze_sentiment
from keyboard_extraction import extract_keywords
from extract_location_time import extract_locations
from azure.cosmos import CosmosClient
from cosmos_db import insert_article
from prometheus_client import start_http_server, Counter

import hashlib
import json

def generate_id(url):
    unique_identifier = hashlib.md5(url.encode()).hexdigest()
    return unique_identifier

def load_config(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)


def on_event(partition_context, event):

    # Prometheus metrics
    data_ingested_counter = Counter('data_ingested_total', 'Total amount of data ingested')
    positive_sentiment_counter = Counter('positive_sentiment_total', 'Total number of articles with positive sentiment')
    negative_sentiment_counter = Counter('negative_sentiment_total', 'Total number of articles with negative sentiment')
    trending_keywords_counter = Counter('trending_keywords_total', 'Total number of trending keywords')
    trending_locations_counter = Counter('trending_locations_total', 'Total number of trending locations')


    try:
        count = 0
        article = json.loads(event.body_as_str().replace("'","\""))  
        article_data = {
            "id": generate_id(article['url']),
            "title": article.get("title"),
            "description": article.get("description"),
            "source": article.get("source").get("name"),
            "url": article.get("url"),
            "publishedAt": article.get("publishedAt"),
            "content": article.get("content"),
            "sentiment": analyze_sentiment(article.get("title"))[0],
            "sentiment_score": analyze_sentiment(article.get("title"))[1],
            "keywords": extract_keywords(article.get("description")),
            "location_time": extract_locations(article.get("description"))
        }
        trending_keywords_counter.inc(len(article_data["keywords"]))
        trending_locations_counter.inc(len(article_data["location_time"]))
        data_ingested_counter.inc()
        
        if article_data["sentiment"] == "positive":
            positive_sentiment_counter.inc()
        elif article_data["sentiment"] == "negative":
            negative_sentiment_counter.inc()

        insert_article(article_data, endpoint, key, database_name, container_name)
        if count == 0:
            print("Received event:", article)
            count = 1
    except Exception as e:
        print("Error:", str(e))

def start_eventhub_consumer(conn_str, event_hub_name, consumer_group, endpoint, key, database_name, container_name ):
    consumer_client = EventHubConsumerClient.from_connection_string(
        conn_str, consumer_group, event_hub_name=event_hub_name
    )

    with consumer_client:
        consumer_client.receive(
            on_event=on_event,
            starting_position="-1",  # Start from the latest event
        )

    
    
    

if __name__ == "__main__":
    

    config = load_config('config.json')
    conn_str = config["conn_str"]
    event_hub_name = config["event_hub_name"]
    consumer_group = config["consumer_group"]
    endpoint = config["endpoint"]
    key = config["key"]
    database_name = config["database_name"] 
    container_name = config["container_name"]

    # Prometheus HTTP server
    start_http_server(8000) 

    start_eventhub_consumer(conn_str, event_hub_name, consumer_group, endpoint, key, database_name, container_name)
