# Autonomocity (DeltaHacks VI)

DevPost: https://devpost.com/software/innovation-factory-c-av#updates

Tackling the challenge presented by Innovation factory; using existing nodes placed on major intersections and congested areas, make use of the live environment data that they provide to connect autonomous vehicles to make the road safer for pedestrians, bikers, drivers, and all users. 

Today's autonomous vehicles are like islands in the sense that they rely on their own sensory systems to view the world and make real time decisions. By connecting autonomous vehicles, we are able to lower the need for a high visibility radius on one singe car. This reduces the engineering and hardware costs of their sensory systems. 

## Proposed methods of connecting autonomous vehicles
- Dynamic speed limits
- Black ice/snow patch detection & safety protocols
- Left turn oncoming traffic indicator
- Blind turn vehicle detection

## Dynamic speed limits
By assessing environment variables like air pressure, temp, humidity, etc. we can make real time small adjustments to the legal speed limit. For e.g., if the air pressure drops, temp drops, and humidity increase, it is most likely raining or about to rain, which is when we would lower the speed limit. 

##  Black ice/snow patch detection & safety protocols
Using a DL algorithm like the Yolo algorithm, in combination with a CNN, we can detect and locate patches of ice/snow on the road. From there we can triangulate the distance of the ice/snow from the car and use basic kinematics to make a protocol describing what speed to decelerate to, for how long, and when it is safe to speed back up. 
