from machine import Pin
import time

# Define pins for the LEDs
led1 = Pin(28,Pin.OUT)
led2 = Pin(27,Pin.OUT)
led3 = Pin(26,Pin.OUT)
led4 = Pin(22,Pin.OUT)
led5 = Pin(21,Pin.OUT)
led6 = Pin(20,Pin.OUT)
led7 = Pin(19,Pin.OUT)
led8 = Pin(18,Pin.OUT)

# Define pins for the buttons 
button1 = Pin(0,Pin.IN,Pin.PULL_UP)
button2 = Pin(1,Pin.IN,Pin.PULL_UP)
button3 = Pin(2,Pin.IN,Pin.PULL_UP)


def st1():
  """
  Turn off all LEDs for 1 second
  """
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    time.sleep(1)


def st2():
  """
  LED chasing effect from right to left
  """
    led8.on()
    led1.off()
    time.sleep(0.5)
    led7.on()
    led8.off()
    time.sleep(0.5)
    led6.on()
    led7.off()
    time.sleep(0.5)
    led5.on()
    led6.off()
    time.sleep(0.5)
    led4.on()
    led5.off()
    time.sleep(0.5)
    led3.on()
    led4.off()
    time.sleep(0.5)
    led2.on()
    led3.off()
    time.sleep(0.5)
    led1.on()
    led2.off()
    time.sleep(0.5)


def st3():
  """
  All LEDs blink on and off togheter
  """
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    led6.on()
    led7.on()
    led8.on()
    time.sleep(0.5)
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    time.sleep(0.5)      


def ask(value1,value2,value3):
    """
    Check the state of the buttons and trigger the corresponding LED pattern
    """
    state1 = value1
    state2 = value2
    state3 = value3

    if state1 == 0:
        st1()
    elif state2 == 0:
        st2()
    elif state3 == 0:
        st3()  

while 1:
    # run a simple animation + constantly check buttons during the sequence
    ask(button1.value(),button2.value(),button3.value())
    led1.on()
    ask(button1.value(),button2.value(),button3.value())
    led8.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led2.on()
    ask(button1.value(),button2.value(),button3.value())
    led1.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led3.on()
    ask(button1.value(),button2.value(),button3.value())
    led2.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led4.on()
    ask(button1.value(),button2.value(),button3.value())
    led3.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led5.on()
    ask(button1.value(),button2.value(),button3.value())
    led4.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led6.on()
    ask(button1.value(),button2.value(),button3.value())
    led5.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led7.on()
    ask(button1.value(),button2.value(),button3.value())
    led6.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    led8.on()
    ask(button1.value(),button2.value(),button3.value())
    led7.off()
    ask(button1.value(),button2.value(),button3.value())
    time.sleep(0.5)
    ask(button1.value(),button2.value(),button3.value())
    
