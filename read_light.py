from machine import ADC
from machine import Pin
import time
Dark = 1000
Light = 0

LightSensorPin = 'P16' # sensor connected to P16. Valid pins are P13 to P20.

lightPin = Pin(LightSensorPin, mode=Pin.IN)  # set up pin mode to input
#
adc = ADC(bits=10)             # create an ADC object bits=10 means range 0-1024 the lower value the less light detected
apin = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)   # create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
time.sleep(1)


def get_light():
    result = apin()
    #print('Light:', result)
    return result

def get_light_perc():
    result = (1-(apin()-Light)/(Dark-Light))*100
    #print('Light level:', result)
    return result



if __name__=="__main__":
    while True:
        val = apin() # read an analog value
        read = (1-(val-Light)/(Dark-Light))*100
        print("Raw value: {0}" .format(val))
        print("Light level: {0:.2f}%" .format(read))
        time.sleep(1)  # wait 1 sec

# Behöver kalibrera dark med nattetid? Och göra funktion...


#def value():
#    val = apin.read()
#    print("Raw value: {0}" .format(val))
#    if result.is_valid():
#        return(result.light)


#while True
#    volts = int(moist_sensor())
#    #pybytes.send_virtual
#   print(volts)
#   sleep(1)
#py.go_to_sleep()
