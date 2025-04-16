from machine import Pin
import time

leds = {
1 : Pin(28,Pin.OUT),
2 : Pin(27,Pin.OUT),
3 : Pin(26,Pin.OUT),
4 : Pin(22,Pin.OUT),
5 : Pin(21,Pin.OUT),
6 : Pin(20,Pin.OUT),
7 : Pin(19,Pin.OUT),
8 : Pin(18,Pin.OUT)
}

button1 = Pin(0,Pin.IN,Pin.PULL_UP)
button2 = Pin(1,Pin.IN,Pin.PULL_UP)
button3 = Pin(2,Pin.IN,Pin.PULL_UP)

def st1():
    for led in range(1,9):
        leds[led].off()
    time.sleep(1)
      
def st2():
    leds[8].on()
    leds[1].off()
    time.sleep(0.5)
    leds[7].on()
    leds[8].off()
    time.sleep(0.5)
    leds[6].on()
    leds[7].off()
    time.sleep(0.5)
    leds[5].on()
    leds[6].off()
    time.sleep(0.5)
    leds[4].on()
    leds[5].off()
    time.sleep(0.5)
    leds[3].on()
    leds[4].off()
    time.sleep(0.5)
    leds[2].on()
    leds[3].off()
    time.sleep(0.5)
    leds[1].on()
    leds[2].off()
    time.sleep(0.5)

def st3():
    for led in range(1,9):
        leds[led].on()
    time.sleep(0.5)
    for led in range(1,9):
        leds[led].off()
    time.sleep(0.5)      
    
def ask(value1,value2,value3):

    if value1 == 0:
        st1()
    elif value2 == 0:
        st2()
    elif value3 == 0:
        st3()  

while 1:
    
    ask(button1.value(),button2.value(),button3.value())
    leds[1].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[8].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[2].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[1].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[3].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[2].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[4].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[3].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[5].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[4].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[6].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[5].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[7].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[6].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    leds[8].on()
    ask(button1.value(),button2.value(),button3.value())
    leds[7].off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
  
