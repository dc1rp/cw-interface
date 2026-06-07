import time
import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode, LEDCode
from machine import Pin
from led import LED, Color
from config import Config

led = LED()
config = Config.load()

last_ms = 0
keys = []
prev_keys = [None]

def pin_callback(pin):
    global last_ms
    global keys
    global prev_keys
    
    now = time.ticks_ms()
    if time.ticks_diff(now, last_ms) < config.debounce_ms:
        return
    last_ms = now

    keys.clear()
    
    [keys.append(code) for pin, code in KEYS if pin.value() == 0]
            
    if keys != prev_keys:
        keyboard.send_keys(keys)
        prev_keys.clear()
        prev_keys.extend(keys)

KEYS = (
    (Pin(config.dot_key), KeyCode.DOT),
    (Pin(config.minus_key), KeyCode.KP_MINUS),
)

[pin.init(Pin.IN, Pin.PULL_UP) for pin, _ in KEYS]

led.set(Color.RED)
time.sleep(1)

if Pin(0).value() == 0:
    led.set(Color.CYAN)
    config.dot_key = 0
    config.minus_key = 1
    config.save()
    time.sleep(1)
elif Pin(1).value() == 0:
    led.set(Color.MAGENTA)
    config.dot_key = 1
    config.minus_key = 0
    config.save()
    time.sleep(1)

[pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pin_callback) for pin, _ in KEYS]
keyboard = KeyboardInterface()
usb.device.get().init(keyboard, builtin_driver=True)

while not keyboard.is_open():
    time.sleep(1)

led.set(Color.GREEN)

while True:
    time.sleep(.5)

