import time
import picamera
camera=picamera.Picamera()
for i in range(5):
    time.sleep(2)
    camera.capture('..')
    print("Image Captured Successfully")
camera.close()