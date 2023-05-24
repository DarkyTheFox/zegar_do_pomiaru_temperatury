# Default sets is 10 display, seven segments
# shift_register -> 74hc595 IC

import machine
import time

# select_mode "SPI" or "GPIO" to control shift register
select_mode = "GPIO"
# If debug mode is True print message from code else don't show any information
debug_mode = True
# choose when latch shift register
# "PROG" -> programming latch or "USER" -> user decide when refresh shift register data
latch_mode = "USER"


class shift_reg:
    def __init__(self, data_pin, clock_pin, latch_pin, clear_pin):
        try:
            if select_mode == "GPIO":
                self.dp = machine.Pin(data_pin, machine.Pin.OUT)
                self.clk = machine.Pin(clock_pin, machine.Pin.OUT)
                self.dp.value(0)
                self.clk.value(0)
                if debug_mode:
                    print("Select GPIO to control display")
            elif select_mode == "SPI":
                self.spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0, sck=machine.Pin(clock_pin),
                                       mosi=machine.Pin(data_pin), miso=None)
                if debug_mode:
                    print("Select SPI to control display")
            self.la = machine.Pin(latch_pin, machine.Pin.OUT)
            self.clr = machine.Pin(clear_pin, machine.Pin.OUT)
            self.la.value(0)
        except:
            if debug_mode:
                print("Error begin initialization display pin control!!!!")

    def clear(self):
        # clear shift register
        self.clr.low()
        self.clr.high()

    def tick(self):
        # tick the clock pin
        self.clk.low()
        self.clk.high()

    def latch(self):
        # flip the latch pin
        self.la.high()
        self.la.low()

    def write(self, value, user_latch):
        if select_mode == "GPIO":
            for i in range(8):
                data = value >> i & 1
                if debug_mode:
                    print("data is", data)
                if data == 0:
                    self.dp.high()
                else:
                    self.dp.low()
                self.tick()
            if latch_mode == "PROG":
                self.latch()
            elif latch_mode == "USER":
                if user_latch:
                    self.latch()
            if debug_mode:
                print(value)
        elif select_mode == "SPI":
            self.spi.write(value)
            if latch_mode == "PROG":
                self.latch()
            elif latch_mode == "USER":
                if user_latch:
                    self.latch()
            if debug_mode:
                print(value)


