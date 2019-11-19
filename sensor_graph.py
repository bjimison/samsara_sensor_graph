import matplotlib.pyplot as plt

class Sensor_Graph():

    def __init__(self, interval, length, sensor):
        self.interval = interval #plotting intervals are in seconds
        self.length = length #length = how many points to show
        self.sensor = sensor

    def begin_plotting(self):
        while True:
            x, y = self.sensor.get_graphing_data(self.length)

            plt.plot(x, y) # plot x and y values found above
            plt.pause(self.interval) # ensures plotting at desired interval
            plt.clf() #clears current axes values, allowing for new axes values        
    