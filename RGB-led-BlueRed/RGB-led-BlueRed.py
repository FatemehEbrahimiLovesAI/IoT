from machine import Pin
import time

green = Pin(1,Pin.OUT)
red = Pin(0,Pin.OUT)
blue = Pin(2,Pin.OUT)

def rgb1(r,g,b):
    red.value(r)
    green.value(g)
    blue.value(b)
    
green2 = Pin(4,Pin.OUT)
red2 = Pin(3,Pin.OUT)
blue2 = Pin(5,Pin.OUT)

def rgb2(r,g,b):
    red2.value(r)
    green2.value(g)
    blue2.value(b)
    
while 1:
    rgb1(1,0,0)
    rgb2(0,0,1)
    time.sleep(0.5)
    rgb1(0,0,1)
    rgb2(1,0,0)
    time.sleep(0.5)
