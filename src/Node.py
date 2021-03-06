## @file Node.py
#  @author Mostafa Mohsen, Chris Vishnu, Seif El Tobgy, Saif Fadhel
#  @brief Provides the Abstract Data Type for Node
#  @date 26/01/2020

import ephem
from Car import *

## @brief A constant that is set to Hamilton on January 26th 2020 for the dewpoint in kelvin
dewpoint = 273

## @brief An ADT that represents a Node
class Node:
    ## @brief Node constructor
    #  @details Initializes a Node object with an empty Node
    #  @param humidity The humidity reported in Percent
    #  @param audio The audio is how strong the rain is by using the sound
    #  @param temperature The temperature reported in Kelvin
    #  @param pressure The pressure reported in Pascals
    #  @param vibration The vibration is the vibration of the node in meters per second
    #  @param video The video is whether or not it is snowing hard or very little
    def __init__(self, humidity, audio, temperature, pressure, vibration, video):
        self.humidity = humidity
        self.audio = audio
        self.temperature = temperature
        self.pressure = pressure
        self.vibration = vibration
        self.video = video

    ## @brief Gets the humidity a Node records
    #  @return returns the humidity
    def get_humidity(self):
    	return self.humidity

    ## @brief Gets the audio a Node records
    #  @return returns the audio
    def get_audio(self):
    	return self.audio

    ## @brief Gets the temperature a Node records
    #  @return returns the temperature
    def get_temperature(self):
    	return self.temperature

    ## @brief Gets the pressure a Node records
    #  @return returns the pressure
    def get_pressure(self):
    	return self.pressure

    ## @brief Gets the vibration a Node records
    #  @return returns the vibration
    def get_vibration(self):
    	return self.vibration

    ## @brief Gets the video a Node records
    #  @return returns the vibration
    def get_video(self):
        return self.video

    ## @brief Checks conditions to determine when rain will occur
    #  @param audio The audio is used to determine hard rain or light rain
    #  @return returns reduced speed by a fractional portion if rain exists and 0 if otherwise
    def determine_rain(self, audio):
        if (self.pressure <= 101325):
            if(audio == "hard rain"):
                return 7/8
            elif(audio == "light rain"):
                return 7.5/8
        return 0

    ## @brief Checks conditions to determine when snow will occur
    #  @param video The video is used to determine heavy snow, light snow, or medium snow
    #  @return returns reduced speed by a fractional portion if snow exists and 0 otherwise
    def determine_snow(self, video):
        if (self.temperature <= 0 and self.pressure <= 101325):
            if(video == "heavy snow"):
                return 5/8
            elif(video == "light snow"):
                return 6/8
            elif(video == "medium snow"):
                return 6/8
        return 0

    ## @brief Checks conditions to determine when fog will occur
    #  @return returns reduced speed by a fractional portion if fog exists and 0 otherwise
    def determine_fog(self):
        if(abs(self.temperature - dewpoint) == 0 and 1 - self.humidity <= 0.1):
            return 5/8
        elif (abs(self.temperature - dewpoint) <= abs(0.1*(self.temperature))):
            if(1 - self.humidity <= 0.1):
                return 6.5/8
        return 0


    ## @brief Checks conditions to determine when wind will occur
    #  @return returns reduced speed by a fractional portion if high wind exists, 1 if windkmh is less than or equal to 25 and 0 otherwise
    def determine_wind(self):
        windkmh = self.vibration * 3.6
        if(windkmh > 45):
            return 4/8
        elif(windkmh > 35 and windkmh <= 45):
	        return 5/8
        elif(windkmh > 25 and windkmh <= 35):
            return 7/8
        elif(windkmh <= 25):
            return 1
        return 0


    ## @brief Checks conditions to determine when the time of day is in the morning or night
    #  @return returns reduced speed by a fractional portion the time of day is night, and 1 if it is in the morning
    def determine_day_and_night(self):
        s = ephem.Sun()
        sf = ephem.city('Toronto')
        s.compute(sf)
        twilight = -12 * ephem.degree
        if s.alt > twilight:
            return 1
        return 7.5/8


    ## @brief Checks conditions to determine by what magnitude to reduce the overall speed by
    #  @car Object of type car that will have its speed modified based on smallest magnitude
    #  @return returns reduced speed based on the smallest magnitude reduced
    def dynamic_speed(self, car):
        snow = self.determine_snow(self.video)
        rain = 0
        if(not snow):
            rain = self.determine_rain(self.audio)
        fog = self.determine_fog()
        wind = self.determine_wind()
        day_and_night = self.determine_day_and_night()

        weather = [snow, rain, fog, wind, day_and_night]
        dspeed = 1
        for i in weather:
            if i != 0:
                if(i < dspeed):
                    dspeed = i
        if(dspeed < 0.5):
            dspeed = 0.5
        car.update_speed(dspeed)
