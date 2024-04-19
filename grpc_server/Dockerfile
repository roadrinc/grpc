FROM python:3.9

WORKDIR /app

# Install supervisord
RUN apt-get update && apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir grpcio grpcio-tools

# Copy the source code and supervisord configuration file
COPY . /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the ports the services listen on
EXPOSE 50051 
EXPOSE 50052

CMD ["/usr/bin/supervisord"]
