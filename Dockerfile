# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files into the container
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
