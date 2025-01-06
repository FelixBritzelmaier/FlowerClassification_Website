# Flower Classification Application

This project uses a pre-trained model to classify flower images. You can run it in **production** using Docker or in **development** locally.

## Development Setup (Windows)

### 1. **Set up Flask App**  
To run the application locally in development mode, follow these steps:

1. Open a command prompt.
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    or
    ```bash
    python -m streamlit run app.py
    ```

Your app should now be running on `http://localhost:8501`.

WARNING : access denied error can appear in development Setup on Windows while trying to delete empty folders in static/uploads. The error disappear in production setup.

## Production Setup (Docker)

### 1. **Build Docker Image**
- size : 9.01GB
- time to install : 5min 4s

To build the Docker image for production, run the following command in the project directory:

```bash
docker build -t flower-classification .
```

### 2. **Run Docker Image**

```bash
docker run -p 8501:8501 flower-classification
```