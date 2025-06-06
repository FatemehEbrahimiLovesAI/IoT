## RGB LED Blinker with MicroPython

This project demonstrates how to control two RGB LEDs using a microcontroller and MicroPython. The script alternates the colors of the LEDs in a blinking pattern.

## Hardware Requirements

* Microcontroller with MicroPython support (e.g., Raspberry Pi Pico)
* 2x Common Cathode RGB LEDs
* 6x Resistors (appropriate for your LEDs, typically 220Ω–330Ω)
* Breadboard and jumper wires

## Pin Configuration

**First RGB LED:**

* Red: GPIO 0
* Green: GPIO 1
* Blue: GPIO 2

**Second RGB LED:**

* Red: GPIO 3
* Green: GPIO 4
* Blue: GPIO 5

## How It Works

* Two functions `rgb1(r, g, b)` and `rgb2(r, g, b)` control the color of the first and second RGB LEDs respectively by setting digital HIGH/LOW on each color pin.
* Inside the infinite loop:

  * The first LED lights up red while the second LED lights up blue.
  * After 0.5 seconds, the colors switch: the first LED becomes blue and the second becomes red.
  * This blinking cycle repeats endlessly.

## Usage

1. Flash MicroPython onto your board.
2. Connect the LEDs to the specified GPIO pins.
3. Upload and run the script using your preferred MicroPython IDE (e.g., Thonny).

## License

This project is open-source and free to use.
