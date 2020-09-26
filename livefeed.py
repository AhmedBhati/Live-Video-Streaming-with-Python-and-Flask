from flask import Flask, render_template, Response,request
import cv2 as cv
from time import sleep
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'vp80')
video=cv.VideoWriter('static/myvideo.webm',fourcc ,6,(320,240))
currentframe=0
app = Flask(__name__, static_folder='static')
@app.route('/')
def index():
    	return render_template('index.html')

def gen():
	#print(cap.read())
	while(cap.isOpened()):
		ret, img = cap.read()
		if ret == True:
			name = str(currentframe)+ '.png'
			img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
			#print(img.shape)
			cv.imwrite(name, img)
			k=(cv.imread(str(currentframe)+'.png'))
			video.write(k)
			frame = cv.imencode('.png', img)[1].tobytes()
			yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
			sleep(0)
		else: 
			break
@app.route('/',methods=['POST'])
def getval():
	k=request.form['psw1']
	if k=='2':
		cap.open(0)
		return render_template("index.html")
	if k=='1':
		cap.release()
		return render_template("index.html")
	if k=='0':
		return render_template("saved.html")
@app.route('/video_feed')
def video_feed():
	return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    	app.run(host='0.0.0.0', debug=False, threaded=True)
