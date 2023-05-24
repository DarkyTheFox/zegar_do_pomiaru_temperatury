import machine
import _thread
import time
import shift_register
import display

led = machine.Pin(25, machine.Pin.OUT)

led.high()
print("start code")

disp = display.display()

while True:
    disp.demo()