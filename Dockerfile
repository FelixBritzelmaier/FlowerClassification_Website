# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install flask torch torchvision pillow timm

# Set environment variable
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Run Flask server
CMD ["python", "app.py"]
