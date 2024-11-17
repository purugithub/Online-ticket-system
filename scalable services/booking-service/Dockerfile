# Booking Service Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5002

# Run the service
CMD ["python", "app.py"]
