# Use official Python lightweight image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (best practice for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app ./app

# Expose Flask port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Start the Flask application
CMD ["python", "app/app.py"]
