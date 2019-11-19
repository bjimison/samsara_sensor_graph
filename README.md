This is a sample application demonstrating how to grab temperature data from a Samsara EM21 or EM22 (Environmental monitors) and display the information on a graph.

Please edit the settings.py to add the widget ID from your EM sensor. You can find the widget ID for any sensor by selecting it from the Samsara Dashboard. The widget ID is at the end of the URL when viewing a temperature sensor.

For example: cloud.samsara.com/o/ORGNAME/WIDGETIDHERE

The groupID and API token can be found in the settings page on your org in the API Tokens section. 

Quick Start on Mac:

Be sure to install the Matplotlib and requests libraries (you'll need JSON as well, but this library is included in pip so you likely don't need to install this package).

Open terminal window. Type “python3 ” then drag the main.py file into the terminal window and hit enter to run the program.