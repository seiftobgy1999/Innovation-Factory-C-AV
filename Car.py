class Car:
    def __init__(self, ID, speed):
        self.speed = speed
    
    def get_ID(self):
    		return self.ID
    
    def get_speed(self):
        return self.speed
        
    def update_speed(self, newSpeed):
    		self.speed = newSpeed
    
    def __str__(self):
    		return "Car " + str(self.ID) + "'s speed is " + str(self.speed) + "KM/H"