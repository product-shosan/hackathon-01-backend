from gpiozero import LED
from time import sleep

# GPIO 17番ピンにLEDが接続されていると仮定
led = LED(17)

print("LEDを点滅させます。Ctrl+Cで終了します。")

try:
    while True:
        led.on()
        print("ON")
        sleep(1)
        led.off()
        print("OFF")
        sleep(1)
except KeyboardInterrupt:
    print("終了します。")