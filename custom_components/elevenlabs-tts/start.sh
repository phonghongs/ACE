#!/bin/bash
# Start script for ElevenLabs TTS component
# This script starts both the event listener and the HTTP server

# Start the HTTP server in the background
python server.py &
SERVER_PID=$!

# Start the event listener in the foreground
python app.py &
APP_PID=$!

# Function to handle termination signals
cleanup() {
    echo "Received termination signal. Shutting down..."
    kill $SERVER_PID
    kill $APP_PID
    exit 0
}

# Register the cleanup function for termination signals
trap cleanup SIGTERM SIGINT

# Wait for both processes
wait $APP_PID $SERVER_PID
