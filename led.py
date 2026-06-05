from machine import Pin
from neopixel import NeoPixel

class Color:
    RED = (10,0,0)
    GREEN = (0,10,0)
    BLUE = (0,0,10)
    WHITE = (10,10,10)
    CYAN = (0,10,10)
    YELLOW = (10,10,0)
    MAGENTA = (10,0,10)
    BLACK = (0,0,0)



class LED:
    def __init__(self):
        self.led = NeoPixel(Pin(16, Pin.OUT), 1)
        
    def set(self, color: Color):
        self.led.fill(color)
        self.led.write()
        
    def off(self):
        self.set(Color.BLACK)
        