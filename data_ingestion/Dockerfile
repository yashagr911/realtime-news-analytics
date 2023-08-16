FROM python:3.8 As data_ingestion

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies (for Python, you would have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the script
CMD ["python", "fetch_and_send_news_to_eventhub.py"]
