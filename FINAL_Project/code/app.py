#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request
import remote_Servo_Control
import camera_pi

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    #from camera import Camera

# Raspberry Pi camera module (requires picamera package)
    from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/controls', methods=['POST'])
def control():
    return remote_Servo_Control.PrintData()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/photo', methods=['POST'])
def photo():
    return camera_pi.takePhoto()

@app.route('/video', methods=['POST'])
def video():
    return camera_pi.takeVideo()


@app.route('/video_feed')
def video_feed():

    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
