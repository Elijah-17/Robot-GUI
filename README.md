# Robot-GUI
GUI for controlling and interfacing with an external robotic arm. This program is to be run on a pi with an external 6 axis robotic arm. 

### The Plan
My goal is to create a GUI for simulating and controlling a 6 axis robotic arm. I have created a section for viewing the robot, a section for controlling and activation, and a section for the program tree. 
I have no idea how to do this and I have never used python or the tkinter GUI library before so this will be fun. 

### How to Use
There is a single executable file (application file) that can be opened to run this program.
or run in vs code after importing 'tkinter', 'customtkinter', 'PIL Image'. This is designed to eventually be uploaded to a Pi with an external display and motor controllers. 
 

### The program
The program opens with a simulation viewer(webcam) and an activate button on the left side and joint sliders on the right.
There is an activate button under the simulation viewer, when activation sucessful, button is replaced by 'Robot connected'
There are joint position sliders on the right side that allow the joints to be controlled 

there is also a program button/tab to open another section of the gui that has programming specific controlls, it shrinks the simulation and has a teach mode. This mode 

 moving the sliders moves the joints. 


I want to have a scrollable area for the program. This would include a teach button, runMode dropdown and run button. 
I plan to have a drop down with a run selection mode, this run selection mode also has a run button so that I can select if I want to run step by step and have to press run for the robot to go to then next taught position, or to run automatically through all the steps. 

# About The Robot
6 axis robotic arm with a
Included joints and their naming scheme and function 
| Joint Name | Number | Function|
| :---------:|:------:|:-------:|
| base     |    1       |    to rotate the robot around the base   |
| shoulder   | 2        |To rotate the arm up and down|
|  elbow |  3 |  to rotate the elbow up and down |
|  forearm |  4 |  rotate forearm around |
| wrist1  |  5 |  rotate tool up and down |
| wrist2  |  6 | to rotate the tool  |

End of arm tooling options
|Gripper Name| Style|Gripper Function|
|:----------:|:----:|:----:|
|3 Finger Gripper|centre in 2 directions| 3 fingers that moving towards eachother to close|
|Parallel Gripper| centre in 1 direction|2 parallel jaws that move towars eachother to close|
|Vacuum Gripper| centre vertically to suction cup| suction cup to create negative air pressure and adhere object to 1 or more cups|

### Controlling Robotic Arm
I have started the file named 'RobotCode' where the 
I am going to have a target x and a current x, I set the target x to be the x of the slider(1 decimal place) and the current x comes from encoders, the percent displayed is the current robot positions, there is a 'wait for' command between the steps to make sure the robot reaches the target within a tolerance before moving in to the next. Depending on the motors and drivers used, PID tuning may be used to increase the precision and decrease the joint stress and movement time. 

### List Of Steps
- [x] create initial readme file 
- [x] create and test the main application with a simple button and frame
- [x] add pseudocode and placeholder comments for future use
- [x] create the frame layout
- [x] create the activate and connection sequence. 
- [x] create functions for the sliders
- [x] add + and - buttons with set values per joint
- [x] convert the function to a class
- [x] add a 'home' button to reset the robot and sliders back to home position
- [x] add webcam for view of the robot
- [x] add gripper activation, selection and controlls 
- [x] add scrollable capability to the program frame
- [ ] add a teach button and runmode dropdowns and '>' button for the robot to run the program
- [ ] add button for adding I/O controlls like setting gripper to be open or closed
- [ ] allow for changes once the program has been made or during the process
- [ ] add file drowdown and a save button to save the program
- [ ] add a close under the save to deactivate robot, lock joints and close the application
- [ ] create the .exe application file
- [ ] write all the robot code to interact with the gui
- [ ] make this Pi friendly and able to fully opperate from 1 pi and touch display

# Future Plans
### GUI Future Plans
There is a lot to improve to say the least. The code is terribly inneficient and takes a long time to open the fairly simple program. I still need to add in another webcam for the gripper view. This would include adding another parameter to the calss for if the gripper has a camera or not. I also need to add more to the program tree to allow for more complex programming with the addition of I/O integration and boolean logic. This would allow the robot to better integrate with external devices. 
### Robot Code Future Plans
Well there are a lot. 'RobotCode' was mostly created as a placeholder file for where all the robot code will eventually go. This file is far from complete and only includes some basic functions that are required for the GUI to function. There is often a console log in place of robot opperations. I still need the initial robot startup sequence and homing and to ensure integration with the GUI is working.