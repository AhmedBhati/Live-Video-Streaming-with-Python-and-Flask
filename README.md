# Live-Video-Streaming-with-Python-and-Flask
In this project Live Video Streaming is Done with Python Using Flask and Gunicorn as a production WSGI server with gevent for asynchronous calls. It streams the video and also saves the stream. All thanks to the the article written by Miguel Grinberg.

Following depencencies should be installed before running the code:
```python
 pip3 install opencv-python	
 pip3 install flask
 pip3 install gunicorn (This cannot be installed in Windows)
 pip3 install gevent (This cannot be installed in Windows)
```

### Download the repository, Open the folder in the terminal.
#### In Ubuntu:

Without Gunicorn and Gevent Install Run:

```
export FLASK_APP=livefeed.py
flask run
```
With Gunicorn:

```
gunicorn --threads 5 --workers 1 --bind 0.0.0.0:5000 livefeed:app
```
With Gunicorn and Gevent(For Making Asynchronous calls):
```
gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 livefeed:app
```
#### In Windows:

```
python3 livefeed.py
```

## Port Forwarding

#### In Ubuntu:

I have used ngrok http tunnel. For that, 
Download the ngrok from its website, the steps are pretty forward and is provided in thier website itself. 
After the procedure is completed open the path where ngrok is extracted and run 
``` 
./ngrok http http://127.0.0.1:8000/ --bind-tls true
```
Just replace the local host port address by your port address 

#### In Windows

Install flask-ngrok
```
pip install flask-ngrok
```
And add this before app.run() in the code

```python
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)
```
