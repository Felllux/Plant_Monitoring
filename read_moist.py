import machine
from time import sleep
# First defining the max and min from previous calibrations,
# which will be the lowest and highest values found
air = 2400
water = 640

adc = machine.ADC()             # create an ADC object
adc.init(bits=12)
apin = adc.channel(pin='P18', attn = machine.ADC.ATTN_11DB)   # create an analog pin on P13, range 0..3.3V

# Defining and fetching moisture data
def get_moist():
    result = apin()
    #print('Moisture:', result)
    return result

# Defining and fetching percentage of moisture
def get_moist_perc():
    result = (1-(apin()-water)/(air-water))*100
    #print('Moisture level:', result)
    return result

    if __name__=="__main__":
        while True:
            val = apin()                    # read an analog value
            read = (1-(val-water)/(air-water))*100
            print("Raw value: {0}" .format(val))
            print("Moisture level: {0:.2f}%" .format(read))
            #print("Moisture level:" .round(read,1), "%")
            sleep(5)

#def moist_sensor():
#    p_out.value(1)
#
#    sleep(0.5)
#    volts = apin.value()
#    p.out.value(0)
#    return volts
#
#while True
#    volts = int(moist_sensor())
#    #pybytes.send_virtual
#   print(volts)
#   sleep(1)
#py.go_to_sleep()
