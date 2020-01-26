from Car import *
from Node import *

def main():
    car1 = Car(101, 80)
    video = ""
    audio = ""
    while(True):
       temp = float(input("What is the current temperature in kelvin? "))
       hum = float(input("What is the current humidity in decimal? "))
       pressure = float(input("What is the current atomospheric pressure in pascals? "))
       vibration = float(input("What is the vibration in meters/s? "))
       if(pressure <= 101325):
           if(temp <= 0):
               video = input("What is the snow level? ")
           else:
               audio = input("Is it raining very hard? ")

       node1 = Node(hum, audio, temp, pressure, vibration, video)
       print("Current Speed", car1.get_speed())
       node1.dynamic_speed(car1)
       print("New Speed", car1.get_speed())


main()
