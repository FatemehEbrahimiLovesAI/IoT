from machine import Pin
import time

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(3, Pin.OUT)
led5 = Pin(4, Pin.OUT)
led6 = Pin(5, Pin.OUT)
led7 = Pin(6, Pin.OUT)
led8 = Pin(7, Pin.OUT)

original_leds = [led1, led2, led3, led4, led5, led6, led7, led8]

def josephus(leds, k, index):
    while len(leds) > 1:
        index = (index + k) % len(leds)
        leds[index].off()
        print(f"LED {index} eliminated.")
        time.sleep(0.5)
        leds.pop(index)

    print(f"LED {leds[0]} is the survivor!")
    leds[0].on()


while True:
    leds = original_leds[:]  
    for led in leds:
        led.on()
    time.sleep(1)
    josephus(leds, 5, 0)
    time.sleep(3)
