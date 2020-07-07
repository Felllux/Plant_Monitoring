from dht import DHT
from machine import Pin
import time

# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(1)

# Example for both RH & temp
#def value():
#    result = th.read()
#    print('Temp:', result.temperature)
#    print('RH:', result.humidity)
#    if result.is_valid():
#        return(result.temperature,result.humidity)

# Reading the temperature
def dht_get_temp():
    result = th.read()
    #print('Temp:', result.temperature)
    time.sleep(2)
    if result.is_valid():
        return(result.temperature)

# Reading the humidity
def dht_get_humid():
    result = th.read()
    #print('RH:', result.humidity)
    time.sleep(2)
    if result.is_valid():
        return(result.humidity)

# function that occurs if you run this file as "main"
if __name__=="__main__":
    print('hello world')
    print(dht_get_humid())
    print(dht_get_temp())
