
from azure.cosmos import CosmosClient
from modules import analyze_sentiment 
import hashlib



def insert_article(data, endpoint, key, database_name, container_name):
    
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    container.create_item(body=data)



def try_query(endpoint, key, database_name, container_name):
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    query = "SELECT * FROM c WHERE c.category = 'movies'"
    items = list(container.query_items(query, enable_cross_partition_query=True))
    for item in items:
        print(item)
