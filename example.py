from pyKUKA import pyKUKA	

myRobot  = pyKUKA("ExampleProgramName")

#Coordinates of the end of the tool relative to the end of the robot arm
myRobot.setToolCoordinates(145,0,86,0,90,0)

#Coordinates relative to robot in milimeters of the origin of the program.
myRobot.setBaseCoordinates(-100,1600,828,-90,0,0)


myRobot.saveFile("example.src")
