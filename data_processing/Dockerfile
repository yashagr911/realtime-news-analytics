FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies (for Python, you would have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into the container
COPY . .

# run command
CMD ["python", "news_analysis_script.py"]
