# User Service Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt
# RUN pip install Flask==2.1.2 Werkzeug==2.1.2

# Expose port
EXPOSE 5001

# Run the service
CMD ["python", "app.py"]
