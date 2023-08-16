import datetime as dt
from azure.eventhub import EventHubProducerClient, EventData
from newsapi import NewsApiClient
import json

def load_config(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)



def fetch_and_send_news_to_eventhub(api_key, connection_string, eventhub_name):
    """
    Fetches news articles using NewsAPI and sends relevant data to an Azure Event Hub.

    Args:
        api_key (str): NewsAPI API key.
        connection_string (str): Azure Event Hub connection string.
        eventhub_name (str): Name of the Azure Event Hub.

    Returns:
        None
    """

    
    # Initialize NewsAPI client
    api = NewsApiClient(api_key=api_key)

    # Initialize Event Hub producer
    producer = EventHubProducerClient.from_connection_string(connection_string, eventhub_name=eventhub_name)
    event_batch = producer.create_batch()

    # Calculate time range for news articles
    current_time = dt.datetime.now() - dt.timedelta(days=2)
    past_time = current_time - dt.timedelta(minutes=20)

    # Fetch news articles
    data = api.get_everything(
        "art OR dance OR music OR movies OR sports OR France",
        from_param=past_time,
        to=current_time
    )

    # Extract relevant data and send to Event Hub
    for article in data.get("articles", []):
        relevant_data = {
            "title": article.get("title"),
            "description": article.get("description"),
            "source": article.get("source").get("name"),
            "url": article.get("url"),
            "publishedAt": article.get("publishedAt"),
            "content": article.get("content")
        }
        event_data = EventData(body=json.dumps(relevant_data))
        event_batch.add(event_data)

    # Send the batch to Event Hub and close the producer
    producer.send_batch(event_batch)
    producer.close()

# Example usage
if __name__ == "__main__":

    config = load_config('config.json')
    
    news_api_key = config['news_api_key']
    eventhub_conn_str = config['eventhub_conn_str']
    eventhub_name = config['eventhub_name']

    fetch_and_send_news_to_eventhub(news_api_key, eventhub_conn_str, eventhub_name)
