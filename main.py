from gpiozero import MotionSensor
from signal import pause
import time

sensor = MotionSensor(4)

def detected():
    print(f"[{time.strftime('%H:%M:%S')}] Motion Detected!! 人を検知しました！")

def m_stopped():
    print("動きが止まりました")

# イベントの登録
sensor.when_motion = detected
sensor.when_no_motion = m_stopped # 検知が終了したとき用

print("センサー監視開始... (Ctrl+C で終了)")

try:
    pause()
except KeyboardInterrupt:
    print("\n終了します")