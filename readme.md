# Flower Classification Application

This project uses a pre-trained model to classify flower images. You can run it in **production** using Docker or in **development** locally.

To test the application you can use 2 floders :
- `flowers-102-categories-perso`is our training data set.
- `flowers` is a compilation of picture from the web that were recognized by our trained model

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

### Other. **Export app history on OUR computer**

```bash
docker cp <CONTAINER_ID>:/app/static/uploads <PATH_TO_DESTINATION_FOLDER>
```
Example of destination path for Windows : `C:/Users/<USER_NAME>/Downloads`