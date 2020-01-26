from Car import *
from Node import *
 
def main():
    car1 = Car(101, 80)
    video = ""
    audio = ""
    while(True):
       temp = float(input("What is the current temperature? "))
       hum = float(input("What is the current humidity? "))
       pressure = float(input("What is the current atomospheric pressure? "))
       vibration = float(input("What is the vibration? "))
       if(pressure <= 101325):
           if(temp <= 0):
               video = input("What does the current situation look like? ")
           else:
               audio = input("What does it sound like right now? ")

       node1 = Node(hum, audio, temp, pressure, vibration, video)
       print("Current Speed", car1.get_speed())
       node1.dynamic_speed(car1)
       print("New Speed", car1.get_speed())


main()