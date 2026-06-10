import time
import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode, LEDCode
from machine import Pin
from led import LED, Color
from config import Config

led = LED()
config = Config.load()

KEYS = (
    (Pin(config.dot_key),   KeyCode.DOT),
    (Pin(config.minus_key), KeyCode.KP_MINUS),
)

for pin, _ in KEYS:
    pin.init(Pin.IN, Pin.PULL_UP)

led.set(Color.RED)
time.sleep(1)

if not Pin(config.in_1).value():
    led.set(Color.CYAN)
    config.dot_key = config.in_1
    config.minus_key = config.in_2
    config.save()
    time.sleep(1)
elif not Pin(config.in_2).value():
    led.set(Color.MAGENTA)
    config.dot_key = config.in_2
    config.minus_key = config.in_1
    config.save()
    time.sleep(1)

keyboard = KeyboardInterface()
usb.device.get().init(keyboard, builtin_driver=True)

while not keyboard.is_open():
    time.sleep(1)

led.set(Color.GREEN)

while True:
    time.sleep(1/config.poll_frequency)
    keyboard.send_keys([code for p, code in KEYS if p.value() == 0])