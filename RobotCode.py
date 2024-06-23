#this is where the robot code is stored and run
#Robot Code starts here
#this runs on pi using the I/O to actually controll the robot
#this is for future upgrades and not currently working to controll a robot.



def ParallelOpen():
    print('opening')
    #take each motor or solenoic and move them to the open position. Use eithor a limit switch or incremental step count to return to open position.

def ParallelClose():
    print('gripper closing')
    #add current limits or positional distances on the closing so if the gripper draws too much current
    #(ie, the motor has to work really hard when trying to close more), the gripper stops openeing
    #keep track of current place and how closed it is, store this in a variable so the robot knowns how to return to open

def GripperOpen():
    print('gripper opening')
    #take each motor or solenoic and move them to the open position. Use eithor a limit switch or incremental step count to return to open position.

def GripperClose():
    print('gripper closing')
    #add current limits or positional distances on the closing so if the gripper draws too much current
    #(ie, the motor has to work really hard when trying to close more), the gripper stops openeing
    #keep track of current place and how closed it is, store this in a variable so the robot knowns how to return to open

def VacuumOpen():
    print('Vacuum on')
    #when this is called, switch the solenoid or latch to open beore the venturi
def VacuumClose():
    print('vacuume off')
    #when this is called, switch the solenoid or disable the latch(depends if solenoid is spring or solenoid return)

def Teach():
    print("learning current pos.")
    #take all current coordinates of robot joints(or target position if it proves to be reliable) and add them to an array.
    #this array should include the decimal position of each joint. the gripper position is entered manually 