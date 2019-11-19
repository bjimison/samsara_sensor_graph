import time

# bring in the supporting modules we built to run the main.py function
from settings import Constants
from sensor_graph import SensorGraph
from temp_sensor import TempSensor

def main():
    # create the temp sensor object with x,y values 
    temperature_sensor = TempSensor(Constants.group_id, Constants.temp_widget_id)

    # graph object which takes the object above and plots it at interval
    interval = 3 * 60
    graph_points = 10 #amount plotted at any given instance
    sensor_graph = SensorGraph(interval, graph_points, temperature_sensor)

    sensor_graph.begin_plotting()

if __name__ == "__main__":
    main()
