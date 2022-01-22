# KUKA Python

![This is an image](https://jonathanmalott.com/wp-content/uploads/2021/11/1.jpg)
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

myRobot.saveFile("example.src")
```

