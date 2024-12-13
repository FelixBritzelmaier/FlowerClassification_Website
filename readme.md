Production:
    create docker image
        docker build -t flower-classification .
    run docker image
        docker run -p 5000:5000 flower-classification

Development (windows):
set FLASK_APP=app.py
python app.pyS