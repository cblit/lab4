from hal import hal_input_switch as switch
from hal import hal_led as led
import time
from time import sleep

def blinky():
    led.init()
    while 1:
        x=0
        status = switch.read_slide_switch()
        while status==1: 
            led.set_output(0, 1)
            time.sleep(0.25)
            led.set_output(0,0)
            time.sleep(0.25)
            status = switch.read_slide_switch()
            print("LED ON")
        
        while status==0:
            if x < 20
                led.set_output(0, 0)
                time.sleep(0.125)
                led.set_output(0,1)
                time.sleep(0.125)
                x = x + 1
            else 
                led.set_output(0, 0)    
                status = switch.read_slide_switch()
            print("LED OFF")


def main():
    switch.init()
    blinky()
    
if __name__ == "__main__":
    main()