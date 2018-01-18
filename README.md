WeatherStation

A simple App displaying the weather of three cities by extracting the data from a database, which is filled by a python script.
It also stores the information in a log file: tempLog.txt

In order to be able to run the app install the requirements from requirements.txt file and create your own config.py file in the main directory with the following
structure:
city_apis = {
            'api_id_sofia': 'YOUR_CUSTOM_API_FROM_openweathermap.org',
            'api_id_velingrad': 'YOUR_CUSTOM_API_FROM_openweathermap.org',
            'api_id_plovdiv': 'YOUR_CUSTOM_API_FROM_openweathermap.org'
            }

To fill the database with data for the current time run:

python WeatherStationMonitor.py

To start the app, type in command line:

python stationFlask.py

TO DO: Fix web design as currently there is no responsiveness implemented

Created on: Jan, 2017

Created by: Kiril Kyuchukov

Version: 1.0.0