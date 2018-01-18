import requests
import json
import threading
import time
from threading import Thread, Event
import sqlite3
import io
import shutil
import config as config_api

def main():
    while True:
        takeSofia()
        takeVelingrad()
        takePlovdiv()
        time.sleep(1800)

        

def takeVelingrad():
    city = "Velingrad"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +city+ config_api.city_apis['api_id_velingrad'] )
    weather = response.json()
    currentDate = time.strftime("%d.%m.%y %H.%M.%S")
    cityName = weather['name']
    cityWeather = weather['main']['temp']
    cityHumidity = weather['main']['humidity']
    createT(currentDate,cityName,cityWeather,cityHumidity)
    createLog(currentDate,cityName,cityWeather,cityHumidity)
    print("\n",currentDate)
    print("The weather for ", weather['name'])
    print("The temperature is ", weather['main']['temp'])  
    print("The humidity is ", weather['main']['humidity'])


def takeSofia():
    city = "Sofia"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +city+ config_api.city_apis['api_id_sofia'])
    weather = response.json()
    currentDate = time.strftime("%d.%m.%y %H.%M.%S")
    cityName = weather['name']
    cityWeather = weather['main']['temp']    
    cityHumidity = weather['main']['humidity']
    createT(currentDate,cityName,cityWeather,cityHumidity)
    createLog(currentDate,cityName,cityWeather,cityHumidity)
    print("\n",currentDate)
    print("The weather for ", weather['name'])
    print("The temperature is ", weather['main']['temp'])
    print("The humidity is ", weather['main']['humidity'])


def takePlovdiv():
    city = "Plovdiv"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +city+ config_api.city_apis['api_id_plovdiv'])
    weather = response.json()
    currentDate = time.strftime("%d.%m.%y %H.%M.%S")
    cityName = weather['name']
    cityWeather = weather['main']['temp']   
    cityHumidity = weather['main']['humidity']
    createT(currentDate,cityName,cityWeather,cityHumidity)
    createLog(currentDate,cityName,cityWeather,cityHumidity)
    print("\n",currentDate)
    print("The weather for ", weather['name'])
    print("The temperature is ", weather['main']['temp'])
    print("The humidity is ", weather['main']['humidity'])


def createT(date,city,temperature,humidity):
        conn = sqlite3.connect("stationData.db",check_same_thread = False)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS tabl(date NUMERIC,city TEXT, temp REAL, hum REAL)')    
        c.execute("INSERT INTO tabl VALUES (?, ?, ?, ?)", [date, city, temperature, humidity])
        conn.commit()
        c.close()
        conn.close()


def createLog(date,city,temeprature,humidity):
    f = open('tempLog.txt','a')
    f.write("In " + str(city) + " on " + str(date) + " the temp is " + str(temeprature) + " with humidity of " +str(humidity) +  "\n" ) 
    f.close()
    

if __name__ == '__main__':
    main()

    