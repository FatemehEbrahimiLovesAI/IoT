## Josephus LED Elimination - MicroPython Project

This project uses MicroPython and a microcontroller board (like Raspberry Pi Pico) to visually demonstrate the **Josephus Problem** using LEDs.

## Project Description

Eight LEDs are connected to GPIO pins 0 through 7. Once all LEDs are turned on, the Josephus algorithm begins eliminating (turning off) every `k`-th LED in a circular pattern until only one LED remains. That LED stays on to indicate the survivor.

In this implementation, the step count `k` is set to 5.

## Hardware Requirements

* A MicroPython-compatible board (e.g., Raspberry Pi Pico)
* 8 LEDs
* 8 resistors (e.g., 220 ohms)
* Breadboard and jumper wires

## Wiring Diagram

Connect each LED to the corresponding GPIO pin:

```
GPIO 0 --> LED1  
GPIO 1 --> LED2  
...  
GPIO 7 --> LED8  
```

Each LED's anode (long leg) connects to the GPIO pin via a resistor, and the cathode (short leg) connects to GND.

## How It Works

1. All LEDs turn on.
2. The Josephus elimination algorithm starts from index 0.
3. Every 5th LED is turned off and eliminated.
4. The last remaining LED stays on as the survivor.
5. After a short pause, the process repeats from the beginning.

## Code Overview

```python
from machine import Pin
import time

# Initialize 8 LEDs
led1 = Pin(0, Pin.OUT)
...
led8 = Pin(7, Pin.OUT)

# Josephus elimination function
def josephus(leds, k, index):
    ...
```

## Customization

* You can change the `k` value in `josephus(leds, k, index)` to modify the elimination step size.
* You can adjust timing (e.g., `sleep` durations) to speed up or slow down the animation.

## License

This project is free to use and modify.
