#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Create KUKA src files easily in python that run on KUKA KR4 robots.
    AUTHOR: Jonathan Malott (JonathanMalott.com)
    University of Texas at Austin School of Architecture
    v0.3.2 Edited November 15 2021
"""
class kukapython:

    def __init__(self,name):

        self.TOOL_IS_DEFINED = False
        self.BASE_IS_DEFINED = False

        #An Array that will contain all of the commands
        self.code = []

        #add some initial setup stuff
        self.code.append("DEF "+str(name)+"()")
        self.code.append("GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )")


        """
            INTERRUPT

            Description Executes one of the following actions:
                - Activates an interrupt.
                - Deactivates an interrupt.
                - Disables an interrupt.
                - Enables an interrupt.
            Up to 16 interrupts may be active at any one time
            
        """
        #self.code.append("INTERRUPT ON 3")


        self.code.append("$APO.CDIS = 0.5000")
        self.code.append("BAS (#INITMOV,0)")
        self.code.append("BAS (#VEL_PTP,20)")
        self.code.append("BAS (#ACC_PTP,20)")
        self.code.append("")


        """
            Advance run
            The advance run is the maximum number of motion blocks that the robot controller calculates and plans in advance during program execution. The actual
            number is dependent on the capacity of the computer.
            The advance run refers to the current position of the block pointer. It is set via
            the system variable $ADVANCE:
                - Default value: 3
                - Maximum value: 5
            The advance run is required, for example, in order to be able to calculate approximate positioning motions. If $ADVANCE = 0 is set, approximate positioning is not possible.
            Certain statements trigger an advance run stop. These include statements
            that influence the periphery, e.g. OUT statements
        """
        self.code.append("$advance=3")
        


#---------------------------------------------------------------------------
# The following methods are used to set the TOOL
#---------------------------------------------------------------------------
    def setToolNumber(self, toolNumber):
        if(self.TOOL_IS_DEFINED == False):
            self.code.append("$TOOL=TOOL_DATA["+str(toolNumber)+"]")
            self.TOOL_IS_DEFINED = True
            return
        raise Exception('You have already defined a tool. Either use setToolNumber or setToolCoordinates but not both.')


    def setToolCoordinates(self,x,y,z,a,b,c):
        #if(self.TOOL_IS_DEFINED == False):
        if(True):
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
        self.code.append("$VEL.CP="+str(velocity))

    def openFold(self,comment):
        self.code.append(";FOLD "+str(comment))

    def closeFold(self):
        self.code.append(";ENDFOLD")
    
#---------------------------------------------------------------------------
# The following methods deal with inputs and outputs
#---------------------------------------------------------------------------

    def setOutput(self, outputNumber, state):
        self.code.append("$OUT["+str(outputNumber)+"] = "+str(state))
          

    def WAIT(self,waitTime):
        self.code.append("WAIT sec "+str(waitTime))
    

    def PTP(self,a1,a2,a3,a4,a5,a6,e1,e2):
        self.code.append("PTP {A1 "+str(a1)+", A2 "+str(a2)+", A3 "+str(a3)+", A4 "+str(a4)+", A5 "+str(a5)+", A6 "+str(a6)+", E1 "+str(e1)+", E2 "+str(e2)+", E3 0, E4 0, E5 0, E6 0}")
    
    def LIN(self,x,y,z,a,b,c,e1,e2):
        self.code.append("LIN {X "+str(x)+", Y "+str(y)+", Z "+str(z)+", A "+str(a)+", B "+str(b)+", C "+str(c)+", E1 "+str(e1)+", E2 "+str(e2)+"} C_DIS")
    
    def CIRC(self,x1,y1,z1,a1,b1,c1,e11,e21,x2,y2,z2,a2,b2,c2,e12,e22):
        self.code.append("CIRC {X "+str(x1)+", Y "+str(y1)+", Z "+str(z1)+", A "+str(a1)+", B "+str(b1)+", C "+str(c1)+", E1 "+str(e11)+", E2 "+str(e21)+"},{X "+str(x2)+", Y "+str(y2)+", Z "+str(z2)+", A "+str(a2)+", B "+str(b2)+", C "+str(c2)+", E1 "+str(e12)+", E2 "+str(e22)+"} C_DIS")
    


    def LIN_REL(self,x=False,y=False,z=False,a=False,b=False,c=False,e1=False,e2=False):
        st = []
        if(x):
            st.append("X "+str(x))
        if(y):
            st.append("Y "+str(y))
        if(z):
            st.append("Z "+str(z))
        if(a):
            st.append("A "+str(a))
        if(b):
            st.append("B "+str(b))
        if(c):
            st.append("C "+str(c))
        if(e1):
            st.append("E1 "+str(e1))
        if(e2):
            st.append("E2 "+str(e2))
        
        assert len(st) > 0

        app = ""

        for s in range(len(st)-1):
            app += st[s] + ", "
        app += st[-1]

        self.code.append("LIN_REL {"+app+"} C_DIS")

    def PTP_REL(self,a1=False,a2=False,a3=False,a4=False,a5=False,a6=False,e1=False,e2=False):
        st = []
        if(a1):
            st.append("A1 "+str(a1))
        if(a2):
            st.append("A2 "+str(a2))
        if(a3):
            st.append("A3 "+str(a3))
        if(a4):
            st.append("A4 "+str(a4))
        if(a5):
            st.append("A5 "+str(a5))
        if(a6):
            st.append("A6 "+str(a6))
        if(e1):
            st.append("E1 "+str(e1))
        if(e2):
            st.append("E2 "+str(e2))
        
        assert len(st) > 0

        app = ""

        for s in range(len(st)-1):
            app += st[s] + ", "
        app += st[-1]

        self.code.append("PTP_REL {"+app+"} C_DIS")
    

    def COMMENT(self,text):
        self.code.append(";"+str(text))

    def BREAK(self):
        self.code.append("")
    
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
        for line in range(len(self.code)-1):
            fileOut.write(self.code[line] + "\n")

        fileOut.write(self.code[-1])
      
