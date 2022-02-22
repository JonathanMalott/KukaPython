# KUKA Python

![This is an image](https://jonathanmalott.com/wp-content/uploads/2021/12/david-675x450.png)

## Introduction

Kuka Python is a library that allows for the creation of KUKA KR4 control files using simple, friendly python.

## Basic KUKApython program
```python
from pyKUKA import pyKUKA	

myRobot  = pyKUKA("ExampleProgramName")


#Coordinates of the end of the tool relative to the end of the robot arm
myRobot.setToolCoordinates(145,0,86,0,90,0)

#Coordinates relative to robot in milimeters of the origin of the program.
myRobot.setBaseCoordinates(-100,1600,828,-90,0,0)

#Set the speed, expressed as a percentage of the max speed.
myRobot.setVelocity(0.3)

#Before we can do anything, we MUST give the robot an initial state for each axis. Skipping this will throw an error on the robot.
myRobot.PTP(90,-75,100,169,-60,-150,0,180)
 

#Finally, we give it a series of LIN commands to trace out a square in space. The parameters are X,Y,Z A,B,C E1,E2
myRobot.LIN(  0,   0, 400,  0, 0, 180, 0, 180) 
myRobot.LIN(  0, 300, 400,  0, 0, 180, 0, 180) 
myRobot.LIN(300, 300, 400,  0, 0, 180, 0, 180) 
myRobot.LIN(300,   0, 400,  0, 0, 180, 0, 180) 
myRobot.LIN(  0,   0, 400, 90, 0, 180, 0, 180) 


#Show an graph of the robot joints over time to detect if there are singularities or 
myRobot.showAnalysis()

myRobot.saveFile("example.src")
```

