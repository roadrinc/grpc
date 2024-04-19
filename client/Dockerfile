# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    libgrpc-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# grpcio and grpcio-tools for gRPC, requests for HTTP requests, and uvicorn with fastapi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container's workspace.
COPY . /app

# Declare the port number the container should expose.
EXPOSE 7878

# Run the app using uvicorn
CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "7878"]