from Car import *
from Node import *
threshhold = 4.5 #m/s^2

def Protocol(car, node, patch_length, distance, video):
    node.dynamic_speed(car)
    vi = car.get_speed()

    if node.determine_snow(video) != 0:
        vf = vi

    
    else:
        vf = 0.8 * vi

    a = abs((vf**2 - vi**2)/(2 * distance))
    a = min(a, threshhold)
    new = (vi**2 + 2 * a * distance)**0.5
    modifier = new / vi 
    car.update_speed(modifier)

