## @file Car.py
#  @author Mostafa Mohsen, Chris Vishnu, Seif El Tobgy, Saif Fadhel
#  @brief Provides the Abstract Data Type for Car
#  @date 26/01/2020

## @brief An ADT that represents a Car
#  @param ID is a unique identifier that is linked to each car
#  @param speed is the speed of the car
class Car:
    ## @brief this is the initializer method
    def __init__(self, ID, speed):
        self.speed = speed

    ## @brief this method is used to get the unique ID of the car
    # @return the ID of the car
    def get_ID(self):
    		return self.ID

    ## @brief this method is used to get the current speed of the car
    # @return the speed of the car
    def get_speed(self):
        return self.speed

    ## @brief this method is used to update the current speed of the car
    # @param modifier is the multiplier that we apply to the current speed to get to the new speed
    # @return the current of the car after the update
    def update_speed(self, modifier):
    	self.speed *= modifier

    ## @brief this method is return the car object and it's information in the form of a string
    # @return the car's information in the form of a string
    def __str__(self):
    	return "Car " + str(self.ID) + "'s speed is " + str(self.speed) + "KM/H"
