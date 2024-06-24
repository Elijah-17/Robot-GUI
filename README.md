# Robot-GUI
GUI for controlling and interfacing with an external robotic arm. This program is to be run on a pi with an external 6 axis robotic arm. 

## The Plan
My goal is to create a GUI for simulating and controlling a 6 axis robotic arm. I have created a section for viewing the robot, a section for controlling and activation, and a section for the program tree. 
I have no idea how to do this and I have never used python or the tkinter GUI library before so this will be fun. 

## How to run
There is a single executable file (application file) that can be opened to run this program.
or run in vs code after importing 'tkinter', 'customtkinter', 'PIL Image'.
 

## The program
The program opens with a simulation viewer(webcam) and an activate button on the left side and joint sliders on the right.
There is an activate button under the simulation viewer, when activation sucessful, button is replaced by 'Robot connected'
There are joint position sliders on the right side that allow the joints to be controlled 

there is also a program button/tab to open another section of the gui that has programming specific controlls, it shrinks the simulation and has a teach mode. This mode 

 moving the sliders moves the joints. 


I want to have a scrollable area for the program. This would include a teach button, runMode dropdown and run button. 
I plan to have a drop down with a run selection mode, this run selection mode also has a run button so that I can select if I want to run step by step and have to press run for the robot to go to then next taught position, or to run automatically through all the steps. 


## to controll robotic arm 
I am going to have a target x and a current x, I set the target x to be the x of the slider(1 decimal place) and the current x comes from encoders, the percent displayed is the current robot positions, there is a 'wait for' command between the steps to make sure the robot reaches the target within a tolerance before moving in to the next. PID tuning to controll the joints.