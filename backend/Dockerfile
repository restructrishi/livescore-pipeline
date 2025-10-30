# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the scores file into the container
COPY scores.json .

# Expose port 8000
CMD [ "python", "-m", "http.server", "8000" ]