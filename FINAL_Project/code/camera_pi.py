import io
import time
import picamera
from base_camera import BaseCamera
from flask import Flask, render_template, request


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
    
def takePhoto():
    if request.method=='POST':
        with picamera.PiCamera() as camera:
            camera.capture('home/pi')
    return ('', 204)

def takeVideo():
    if request.method=='POST':
        with picamera.PiCamera() as camera:
            camera.start_recording('home/pi')
            time.sleep(10)
            camera.stop_recording()
    return ('', 204)