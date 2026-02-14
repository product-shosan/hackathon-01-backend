from gpiozero import MotionSensor
from signal import pause
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#状態管理用変数
status = {
    "is_occupied": False
}
sensor = MotionSensor(4)

#検知用関数
def detected():
    status["is_occupied"] = True
    print("人を検知しました。")

def m_stopped():
    status["is_occupied"] = False
    print("人を検知しました。")

#関数の割り当て
sensor.when_motion = detected
sensor.when_no_motion = m_stopped 


#APIの作成
app = FastAPI()

#CORSの許可（一旦全許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#GETリクエストの作成
@app.get("/status")
def get_status():
    return status

print("センサー監視開始... (Ctrl+C で終了)")

try:
    pause()
except KeyboardInterrupt:
    print("\n終了します")