# Use the official Python image from the Docker Hub
FROM python:3.9-slim

WORKDIR /app

COPY . /app

WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run load_test/main.py when the container launches
ENTRYPOINT ["python", "load_test/main.py"]