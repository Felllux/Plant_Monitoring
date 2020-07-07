from network import WLAN
import urequests as requests
import machine
import pycom
import time
import read_dht
import read_light
import read_moist
import json


print("Start")

TOKEN = "BBFF-TyjP0JHT6J8tupYsGrSbC4patCO2ow" # Put here your TOKEN from ubidots
DELAY = 600  # Delay in seconds

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)

# Assign your Wi-Fi credentials
wlan.connect("Anzies_wifi", auth=(WLAN.WPA2, "rudechalmers"), timeout=5000)

# connecting to WiFi
while not wlan.isconnected ():
    print("connecting to WiFi...")
    time.sleep(1)
    machine.idle()
print("Connected to Wifi\n")


# the variables defined and fetched from their respective read files
temperature = read_dht.dht_get_temp()
humidity = read_dht.dht_get_humid()
light = read_light.get_light()
light_perc = read_light.get_light_perc()
moist = read_moist.get_moist()
moist_perc = read_moist.get_moist_perc()

# Builds the json to send the request
#def build_json(variable1, value1, variable2, value2, variable3, value3, variable4, value4, variable5, value5, variable6, value6):
#    try:
#        lat = 57.709097  # latitude
#        lng = 11.937518  # longtitude
        # data array creation
#        data = {variable1: {"Temperature": temperature},
#                variable2: {"Humidity": humidity, "context": {"lat": lat, "lng": lng}}, # value - main information, context - additional
#                variable3: {"Light": light},
#                variable4: {"light Percentage": light_perc},
#                variable5: {"Soil Moisture": moist},
#                variable6: {"Soil Moisture Percentage": moist_perc}}
#        return data
#    except:
#        return None

# Builds the json to send the request
def build_json(variable1, value1, variable2, value2, variable3, value3, variable4, value4, variable5, value5, variable6, value6, variable7, value7):
    try:
        lat = 57.709102  # latitude
        lng = 11.937541  # longtitude
        # data array creation
        data = {variable1: {"value": value1},
            variable2: {"value": value2}, # value - main information, context - additional
            variable3: {"value": value3},
            variable4: {"value": value4},
            variable5: {"value": value5},
            variable6: {"value": value6},
            variable7: {"value": value7, "context": {"lat": lat, "lng": lng}}
            }
        return data
    except:
        return None


# Sends the request. Please reference the REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2, value3, value4, value5, value6, value7):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "humidity", value2, "light", value3, "light_perc", value4, "moist", value5, "moist_perc", value6, "position", value7)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data) # include data as JSON object
            return req.json()
        else:
            pass
    except:
        pass

while True:
    print ("Sending data with " + str(DELAY) + " seconds delay")
    # the output printed, with the percentage values for light and moisture
    print('Temperature:', temperature)
    print('Humidity:', humidity)
    print('Light:', light)
    print('Light level: {0}%' .format(light_perc))
    print('Moisture:', moist)
    print('Moisture level: {0:.1f}%' .format(moist_perc))
    pybytes.send_signal(1, temperature)
    pybytes.send_signal(2, humidity)
    pybytes.send_signal(3, light)
    pybytes.send_signal(4, light_perc)
    pybytes.send_signal(5, moist)
    pybytes.send_signal(6, moist_perc)
    post_var("Felix_loPy4", temperature, humidity, light, light_perc, moist, moist_perc, 1)  # send data to UBIDOTS
    time.sleep(DELAY)
