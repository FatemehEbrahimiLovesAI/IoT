from machine import Pin,ADC,I2C
from ssd1306 import SSD1306_I2C
import time

m = ADC(Pin(27))
i2c = I2C(0,scl=Pin(17),sda=Pin(16))
oled = SSD1306_I2C(128,64,i2c)

def oled_write(text,x,y):
    oled.text(text,x,y)
    oled.show()
    
def oled_clear():
    oled.fill(0)
    oled.show()
    
while 1:
    v = m.read_u16()*3.3/65535
    oled_write("Voltage:",68,25)
    oled_write(str(round(v,2)),68,50)
    time.sleep(1)
    oled_clear()
