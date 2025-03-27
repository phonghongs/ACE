FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for PyAudio
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY server.py .
COPY start.sh .
COPY .env .

# Make start script executable
RUN chmod +x start.sh

# Run both the event listener and HTTP server
CMD ["./start.sh"]
