# Robot-GUI
GUI for interfacing with a robot and later connectivity support with an external robotic arm. 

## The Plan
My goal is to create a GUI for simulating and controlling a 6 axis robotic arm. I also plan to simulate tasks and program points in space for the robot to travel to. 
I have no idea how to do this and I have never used python before. 

## How to run
There is a single executable file (application file) that can be opened to run this program. 
 

## The program
The program opens with a simulation viewer and an activate button on the left side and joint sliders on the right.
There is an activate button under the simulation viewer, when activation sucessful, button is replaced by 'Robot connected'
There are joint position sliders on the right side that allow the joints to be controlled 

there is also a program button/tab to open another section of the gui that has programming specific controlls, it shrinks the simulation and has a teach mode. This mode 

 moving the sliders moves the joints. 


I want to have a button called 'program' that opens a second smaller page of the app with joint motion types and a teach button and joint speeds

I plan to have a drop down with a run selection mode, this run selection mode also has a run button so that i can select if i want to run step by step and have to press run to start the next step, or to run automatically through all the steps. 





## to controll robotic arm 
I am going to have a target x and a current x, I set the target x to be the x of the slider(1 decimal place) and the current x comes from encoders, the percent displayed is the current robot positions, there is a 'wait for' command between the steps to make sure the robot reaches the target within a tolerance before moving in to the next. PID tuning to controll the joints.