## @file Snow_protocol.py
#  @author Mostafa Mohsen, Chris Vishnu, Seif El Tobgy, Saif Fadhel
#  @brief Provides function for how to react when apporaching snow patch
#  @date 26/01/2020
from Car import *
from Node import *
threshhold = 4.5 #m/s^2

## @brief Node constructor
#  @param car the car is a object that contains that speed and ID of the vehicle
#  @param node the node is a unit that contains various sensors that measure environmental conditions
#  @param patch_length the length of the patch of snow
#  @param distance the distance from the car to the patch of snow
#  @return a string that represents the set of protocols to follow when you approach a patch of snow
def Protocol(car, node, patch_length, distance):
    node.dynamic_speed(car)
    vi = car.get_speed()

    if node.determine_snow(node.get_video()) != 0:
        vf = vi


    else:
        vf = 0.8 * vi

    a = abs((vf**2 - vi**2)/(2 * distance))
    a = min(a, threshhold)
    new = (vi**2 + 2 * -a * distance)**0.5
    modifier = new / vi
    car.update_speed(modifier)

    return ("initial V = " + str(vi) +  "; accelerate for a = " + str(-a) + "; untill final V = " + str(new))

car1 = Car(10, 80)
node1 = Node(0.5, "he", -1, 1000000, 0, "light snow")
print(Protocol(car1, node1, 30, 50,))
