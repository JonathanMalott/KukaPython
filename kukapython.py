#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Create KUKA src files easily in python that run on KUKA KR4 robots.
    AUTHOR: Jonathan Malott (JonathanMalott.com)
    University of Texas at Austin School of Architecture
"""

class kukapython:

    def __init__(self,name):
        #self.x = x
        #self.y = y
        #self.description = "This shape has not been described yet"
        #self.author = "Nobody has claimed to make this shape yet"

        self.TOOL_IS_DEFINED = False
        self.BASE_IS_DEFINED = False

        self.code = []

        self.code.append("DEF "+str(name)+"()")
        self.code.append("GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )")
        self.code.append("INTERRUPT ON 3")
        self.code.append("$APO.CDIS = 0.5000")
        self.code.append("BAS (#INITMOV,0)")
        self.code.append("BAS (#VEL_PTP,20)")
        self.code.append("BAS (#ACC_PTP,20)")
        self.code.append("")
        

    def perimeter(self):
        return 2 * self.x + 2 * self.y


#---------------------------------------------------------------------------
# The following methods are used to set the TOOL
#---------------------------------------------------------------------------
    def setToolNumber(self, x,y,z,a,b,c):
        if(self.TOOL_IS_DEFINED == False):
            self.code.append("$TOOL=TOOL_DATA[11]")
            self.TOOL_IS_DEFINED = True
            return
        raise Exception('You have already defined a tool. Either use setToolNumber or setToolCoordinates but not both.')


    def setToolCoordinates(self,x,y,z,a,b,c):
        if(self.TOOL_IS_DEFINED == False):
            self.code.append("$TOOL={X "+str(x)+", Y "+str(y)+", Z "+str(z)+", A "+str(a)+", B "+str(b)+", C "+str(c)+"}")
            self.TOOL_IS_DEFINED = True
            return
        raise Exception('You have already defined a tool. Either use setToolNumber or setToolCoordinates but not both.')

#---------------------------------------------------------------------------
# The following methods are used to set the BASE
#---------------------------------------------------------------------------

    def setBaseNumber(self, number):
        if(self.BASE_IS_DEFINED == False):
            self.code.append("$BASE=BASE_DATA["+str(number)+"]")
            self.BASE_IS_DEFINED = True
            return
        raise Exception('You have already defined a base. Either use setToolNumber or setToolCoordinates but not both.')


    def setBaseCoordinates(self,x,y,z,a,b,c):
        if(self.BASE_IS_DEFINED == False):
            self.code.append("$BASE={X "+str(x)+", Y "+str(y)+", Z "+str(z)+", A "+str(a)+", B "+str(b)+", C "+str(c)+"}")
            self.BASE_IS_DEFINED = True
            return
        raise Exception('You have already defined a base. Either use setToolNumber or setToolCoordinates but not both.')

    def setVelocity(self,velocity):
        self.code.append("$advance=5")
        self.code.append("$VEL.CP="+str(velocity))
           
    def PTP(self,a1,a2,a3,a4,a5,a6,e1,e2):
        self.code.append("PTP {A1 "+str(a1)+", A2 "+str(a2)+", A3 "+str(a3)+", A4 "+str(a4)+", A5 "+str(a5)+", A6 "+str(a6)+", E1 "+str(e1)+", E2 "+str(e2)+", E3 0, E4 0, E5 0, E6 0}")
    
    def LIN(self,x,y,z,a,b,c,e1,e2):
        self.code.append("LIN {X "+str(x)+", Y "+str(y)+", Z "+str(z)+", A "+str(a)+", B "+str(b)+", C "+str(c)+", E1 "+str(e1)+", E2 "+str(e2)+"} C_DIS")
    
#---------------------------------------------------------------------------
# Export the code as a file
#---------------------------------------------------------------------------

    def saveFile(self, filename):

        if(self.TOOL_IS_DEFINED == False):
            Exception('You must define a tool')
            return
        if(self.BASE_IS_DEFINED == False):
            Exception('You must define a base')
            return


        #Since we are done adding lines to the program, we will END it
        self.code.append("END")

        #Write each line of the KUKA src program to the specified file
        fileOut = open(filename,"w")
        for line in self.code:
            fileOut.write(line + "\n")
      
