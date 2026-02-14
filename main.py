from gpiozero import MotionSensor
from signal import pause
import time

print("Motion Detected!!")

#関数の設定
def detected():
    a = 'Motion Deteced!!'
    print(a)

sensor = MotionSensor(2)

sensor.when_motion = detected

while 1:
    print('.')
    time.sleep(0.1)

pause()
