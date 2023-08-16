#!/bin/bash

# Install Minikube
echo "Installing Minikube..."
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/

# Install Helm
echo "Installing Helm..."
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

# Install Docker (assuming you're on a Linux distribution that uses APT)
echo "Installing Docker..."
sudo apt-get update
sudo apt-get install -y docker.io

# Start Minikube
echo "Starting Minikube..."
minikube start

# Install Prometheus using Helm
echo "Installing Prometheus..."
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus

# Install Grafana using Helm
echo "Installing Grafana..."
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana

# Create data_ingestion/config.json
echo '{
    "news_api_key": "",
    "eventhub_conn_str": "",
    "eventhub_name": ""
}' > data_ingestion/config.json

# Create data_processing/config.json
echo '{
    "conn_str": "",
    "event_hub_name": "",
    "consumer_group": "$Default",
    "endpoint": "",
    "key": "",
    "database_name": "",
    "container_name": ""
}' > data_processing/config.json

echo "Setup complete!"
