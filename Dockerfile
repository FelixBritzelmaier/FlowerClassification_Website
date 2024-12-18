# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install streamlit torch torchvision pillow timm

# Expose port
EXPOSE 8501

# Run Flask server
CMD ["streamlit", "run", "app.py"]
