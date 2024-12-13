# Flower Classification Application

This project uses a pre-trained model to classify flower images. You can run it in **production** using Docker or in **development** locally.

## Development Setup (Windows)

### 1. **Set up Flask App**  
To run the application locally in development mode, follow these steps:

1. Open a command prompt.
2. Set the `FLASK_APP` environment variable:
    ```bash
    set FLASK_APP=app.py
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

Your app should now be running on `http://127.0.0.1:5000`.

## Production Setup (Docker)

### 1. **Build Docker Image**

To build the Docker image for production, run the following command in the project directory:

```bash
docker build -t flower-classification .
```

### 2. **Run Docker Image**

```bash
docker run -p 5000:5000 flower-classification
```