import cv2
import customtkinter
import tkinter
from PIL import Image, ImageTk
import time
from RobotCode import *


# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x780")
#create frames for portions of window
webCam_frame = customtkinter.CTkFrame(app, width=550, height=600)
webCam_frame.place(x=10, y=10)
program_frame = customtkinter.CTkScrollableFrame(app, width=700, height=700)
program_frame.place(x=800, y=10)
program_controll = customtkinter.CTkFrame(app, width=720, height= 50)
program_controll.place(x=800, y=730)
slider_frame = customtkinter.CTkFrame(app, width=260, height=480)
slider_frame.place(x=530, y=10)
gripper_frame = customtkinter.CTkFrame(app, width=260, height=150)
gripper_frame.place(x=530, y=500)
Activate_frame = customtkinter.CTkFrame(app, width=260, height=75)
Activate_frame.place(x=530, y=660)


allSliders = []

def connect():
    ActivateButton.pack_forget()  # Hide the button
#say connecting to robot... in orange or blue
    text_connecting = customtkinter.CTkLabel(Activate_frame, text="Robot Connecting...", width=260, height=30, text_color="darkorange", bg_color="darkgrey")
    # text_connecting.place(x=225, y=620)
    text_connecting.pack()
    app.update()
    #
    connectRobot()
    #time.sleep(3)#timer in place of robot connection and activation sequence
    #
    #robot homing sequence
    #this will eventually be custom so each joint touches off on its limit switch
    Controll_label = customtkinter.CTkLabel(slider_frame, text= 'Controll')
    Controll_label.pack()
    allSliders.extend([
# Sliders(frame, joint name, slider position, target position, plus/minus button effect
    Sliders(slider_frame, 'Joint 1', 0, 0, 2, 2),
    Sliders(slider_frame, 'Joint 2', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 3', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 4', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 5', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 6', 0, 0, 5, 5)
    ])
    reset_all_sLiders()

    #when connection is failed, add and else condition to the 'try'

    #when succesful connection achieved
    text_connecting.pack_forget()
    text_connected = customtkinter.CTkLabel(Activate_frame, text="Robot Connected", width=260, height=30, text_color="green", bg_color="darkgrey")
    # text_connected.place(x=225, y=620)
    text_connected.pack()
    app.update()

    update_video_feed()

    #labelling the controll areas
    Gripper_label = customtkinter.CTkLabel(gripper_frame, width=260, text= 'Gripper Controll')
    Gripper_label.pack()

    Home_Button = customtkinter.CTkButton(slider_frame, width=75, text='HOME', command=reset_all_sLiders)
    #Home_Button.place(x=500, y=620)
    Home_Button.pack()
    gripper()
    program()
    app.update()

def update_video_feed():
    ret, frame = vid.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        webcam_label.configure(image=img)
        #webcam_label.image = img
    webCam_frame.after(15, update_video_feed)
    
#runs before the robot connects. Adds labels and file menu. 
webcam_label = customtkinter.CTkLabel(webCam_frame)
webcam_label.pack()
# Create a button
ActivateButton = customtkinter.CTkButton(Activate_frame, text="connect", width=260, command=connect)
ActivateButton.pack() 
# ActivateButton.place(x = 200, y = 620)


#
vid = cv2.VideoCapture(0)
#


class gripperOption(customtkinter.CTkFrame):
    def __init__(self, parent, GripperName, OpenName, CloseName, OpenCommand, CloseCommand): 
        super().__init__(master=parent)
        self.GripperName = GripperName
        self.Open = OpenName
        self.Close = CloseName
        self.OpenC = OpenCommand
        self.CloseC = CloseCommand

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.name_label = customtkinter.CTkLabel(self, width=260, height=30, text=GripperName, fg_color='grey', font=("Helvetica", 20))
        self.name_label.grid(row=0, column=0, columnspan=2)

        self.open_button = customtkinter.CTkButton(self, width = 75, height=30, text=self.Open, command= self.OpenC)
        self.open_button.grid(row=1, column=0)

        self.close_button = customtkinter.CTkButton(self, width = 75, height=30, text=self.Close, command=self.CloseC)
        self.close_button.grid(row=1, column=1) 
        self.pack(expand = False)

#on and off text is different for vacume. vacume is on/off, normal grippers are open/close. The buttons use these labels 
# and set a boolean called eithor 'open' or 'close'. on sets the gripper to true, off sets the gripper to false.

def fingerActivate():
    gripper_Select.pack_forget()
    gripperOption(gripper_frame, '3 finger gripper', 'OPEN', 'CLOSE', GripperOpen, GripperClose)

def ParallelActivate():
    gripper_Select.pack_forget()
    gripperOption(gripper_frame, 'parallel gripper', 'OPEN', 'CLOSE', ParallelOpen, ParallelClose)

def VacuumActivate():
    gripper_Select.pack_forget()
    gripperOption(gripper_frame, 'Vacuum gripper', 'ON', 'OFF', VacuumOpen, VacuumClose)

def option(choice):
    if choice == '3 Finger':
        fingerActivate()
    elif choice == 'Parallel Jaw':
        ParallelActivate()
    elif choice == 'Vacuum':
        VacuumActivate()
 
def gripper():

    # print('gripper')
    options = [
        'select',
        '3 Finger',
        'Parallel Jaw',
        'Vacuum'
    ]
    clicked = customtkinter.StringVar()
    clicked.set(options[0])  # Set the default value
    global gripper_Select
    gripper_Select = customtkinter.CTkOptionMenu(gripper_frame, variable=clicked, values=options, command=option)
    gripper_Select.pack()


 # Function to update slider percentage

class Sliders(customtkinter.CTkFrame):
    def __init__(self, parent, joint_name, slider_position, target_position, plus, minus): #joint_coordinate, 
        super().__init__(master=parent)
        self.target_position = target_position
        self.plus = plus
        self.minus = minus
        self.original_position = -5


        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0,1,2), weight=1)

        customtkinter.CTkLabel(self, text=joint_name).grid(row=0, column=0)
        self.slider = customtkinter.CTkSlider(self, from_=-50, to=50, command=self.update_from_slider)
        self.slider.set(slider_position)
        self.slider.grid(row=1, column=1)
       
        #when using robotic arm, use line 31 and comment out 32 & 33.
        #customtkinter.CTkLabel(self, text=joint_coordinate).grid(row=0, column=4)
        self.target_label = customtkinter.CTkLabel(self, text=str(self.target_position))
        self.target_label.grid(row=0, column=2)

        customtkinter.CTkButton(self, text='+', width=10, height =20, command=self.increase).grid(row=1, column=2)
        customtkinter.CTkButton(self, text='-', width=10, height =20, command=self.decrease).grid(row=1, column=0)

        self.pack(pady=10) #(expand = True, padx=10, pady=10)
        self.grid_location(x=500, y=30)
#functions to make the +/- buttons work and to correctly display the values
    def increase(self):
        self.target_position += self.plus
        self.update_display()

    def decrease(self):
        self.target_position -= self.minus
        self.update_display()

    def update_display(self):
        self.target_label.configure(text=str(self.target_position))
        self.slider.set(self.target_position)

    def update_from_slider(self, value):
        self.target_position = int(value)
        self.update_display()
        
    def home(self):
        self.target_position = self.original_position
        self.update_display()

def reset_all_sLiders():
    print('HOMING')
    for sliders in allSliders:
        sliders.home()
    app.update

def program():
    print('program')
    program_label = customtkinter.CTkLabel(program_frame, width=700, height=30, text="Program")
    program_label.pack()
#Using the teach button, make a program tree from the list of taught points. 
# make a function or a class to print out each taught joint point on the screen with motion speeds and I/O controll like gripper open/close

    # create buttons for 'teach' and '>'(run)
    teach = customtkinter.CTkButton(program_controll, width=50, height=20, text='Teach', command=Teach)
    teach.grid(row=0, column=0, padx=10, pady=10)
    space = customtkinter.CTkLabel(program_controll, width=430, height=20, text='')
    space.grid(row=0, column=2)
    run = customtkinter.CTkButton(program_controll, width=40, height=40, text= '>', command= Run)
    run.grid(row=0, column=4, padx=10, pady=10)

    #creating the runmode dropdowns and their options
    optionsRun = [
        'select',
        'Step Mode',
        'Automatic'
    ]
    clickedRun = customtkinter.StringVar()
    clickedRun.set(optionsRun[0])  # Set the default value
    runmode = customtkinter.CTkOptionMenu(program_controll, height=40, variable=clickedRun, values=optionsRun)
    runmode.grid(row=0, column=3, rowspan=2, padx=10, pady=10)
    print('clicking')
    print(clickedRun)


    # # creating the I/O dropdown and options
    # optionsio = [
    #     'select',
    #     'gripper'
    # ]
    # clickedio = customtkinter.StringVar()
    # clickedio.set(optionsio[0])  # Set the default value
    # io = customtkinter.CTkOptionMenu(program_controll, height=20, variable=clickedio, values=optionsio)
    # io.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

    # create dropdowns for runmode and I/O
    #this is where the program tree is made and controlled, i definately dont know the best way to do this especially with the scrollable
    #frame. Or how to display multiple taught positions. Could use a class called 'displayProgram' and feed in the positions from the teach
    #function. I dont know for sure but this might work. 

app.mainloop()
vid.release()
