import json
import requests # so we can make POST request to API

from datetime import datetime
from settings import Constants

class TempSensor():
    # create dunder method to construct instance of Temp Sensor
    def __init__(self, group_id, sensor_id):
        self.sensor_id = sensor_id
        self.group_id = group_id
        self.name = "" # name retrieved from API
        self.vehicleId = "" # vehicle ID retrieve from API
        self.x = [] # time of recorded temp data
        self.y = [] # temp values
    
    # The API returns values in Celsius, lets convert to Fahrenheit
    def celsiusToFahrenheit(self, celsius):
        return (celsius * (9/5)) + 32

    def beginSensing(self):
        # create a POST request in JSON format
        body = {
            "groupId": self.group_id,
            "sensors": [self.sensor_id]
        }

        params = {
            "access_token": Constants.access_token
        }

        response = requests.post(Constants.temperature_end_point, params = params, json=body)

        if response.status_code != 200:
            raise Exception("Non OK status code returned:", response.text)
            # using raise exception here as we are not looking for syntax errors, but execution errors

        #jsonify the response so we can extract
        response = response.json

        sensor_data = response["sensors"][0]
        self.name = sensor_data["name"]
        self.vehicleId = sensor_data["vehicleId"]
        # using the api_time_format we entered in settings
        time = datetime.strptime(sensor_data["ambientTemperatureTime"], Constants.api_time_format)
        self.x.append(time.strftime("%d-%b-%y %H:%M"))
        # API returns millicelsius, so we need to divide by 1000 to get Celsius
        temp = sensor_data["ambientTemperature"] / 1000
        self.y.append(self.celsiusToFahrenheit(temp))

    def get_graphing_data(self, length):
        self.beginSensing()
        return self.x[-length:], self.y[-length:]
