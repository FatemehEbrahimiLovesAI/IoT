# Analog Voltage Display with OLED on Raspberry Pi Pico

This project reads an analog voltage using an ADC pin on the Raspberry Pi Pico and displays the value on a 128x64 SSD1306 OLED display over I2C.

## Features

- Reads analog voltage from GPIO 27.
- Displays the voltage (0.00 – 3.30V) on an SSD1306 OLED.
- OLED automatically updates every second.

## Hardware Required

- Raspberry Pi Pico (or compatible)
- SSD1306 OLED Display (128x64, I2C interface)
- Analog voltage source (e.g., potentiometer or sensor)
- Jumper wires

## Wiring

| Component       | Pico Pin | Description     |
|----------------|----------|-----------------|
| OLED VCC       | 3.3V     | Power Supply    |
| OLED GND       | GND      | Ground          |
| OLED SDA       | GP16     | I2C Data        |
| OLED SCL       | GP17     | I2C Clock       |
| Analog Input   | GP27     | ADC Input       |

## Software Requirements

- MicroPython firmware on the Raspberry Pi Pico
- `ssd1306.py` driver file uploaded to the Pico
- Thonny IDE or any MicroPython-compatible environment

## How to Run

1. Flash your Pico with the latest MicroPython firmware.
2. Upload both this script and the `ssd1306.py` driver to your Pico.
3. Connect the components as per the wiring diagram.
4. Run the script from your development environment.

The OLED screen should begin displaying the real-time analog voltage.

## Code Overview

The script:
- Initializes the ADC on pin 27
- Sets up I2C and the OLED
- Reads the analog value, converts it to voltage
- Displays it on the OLED
- Refreshes every second

## License

This project is open-source and free to use.

## Author

Created by Fatemeh Ebrahimi
