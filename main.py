import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode, LEDCode
from machine import Pin
import time

last_ms = 0
DEBOUNCE_MS = 3

keys = []
prev_keys = [None]

def pin_callback(pin):
    global last_ms
    global keys
    global prev_keys
    
    now = time.ticks_ms()
    if time.ticks_diff(now, last_ms) < DEBOUNCE_MS:
        return
    last_ms = now

    keys.clear()
    
    for pin, code in KEYS:
        if pin.value() == 0:
            keys.append(code)
            
    if keys != prev_keys:
        k.send_keys(keys)
        prev_keys.clear()
        prev_keys.extend(keys)

KEYS = (
    (Pin(0), KeyCode.DOT),
    (Pin(1), KeyCode.KP_MINUS),
)

for pin, _ in KEYS:
    pin.init(Pin.IN, Pin.PULL_UP)
    pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pin_callback)

led = machine.Pin(25, machine.Pin.OUT)

k = KeyboardInterface()
usb.device.get().init(k, builtin_driver=True)

while not k.is_open():
    time.sleep(1)

led.value(1)

while True:
    time.sleep(1)
