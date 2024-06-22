import cv2
import customtkinter
import tkinter
from PIL import Image, ImageTk
import time


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
program_frame = customtkinter.CTkFrame(app, width=550, height=600)
program_frame.place(x=800, y=10)
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
gripperOption(gripper_frame, '3 finger gripper', 'OPEN', 'Close')
grippetOption(gripper_frame, 'parallel gripper', 'Open', 'close')
gripperOption(gripper_frame, 'vacuume gripper', 'on', 'off')

class gripperOption(customtkinter.CTkFrame):
    def __init__(self, parent, GripperName, OpenName, CloseName): #joint_coordinate, 
        super().__init__(master=parent)
        self.GripperName = GripperName
        self.Open = OpenName
        self.Close = CloseName

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0,1,2), weight=1)
        name = customtkinter.CTkLabel(gripper_frame, width = 260, height=20, text=GripperName, bg_color='grey')
        name.grid(row=0, column=1)
#on and off text is different for vacume. vacume is on/off, normal grippers are open/close. The buttons use these labels 
# and set a boolean called eithor 'open' or 'close'. on sets the gripper to true, off sets the gripper to false.

    if GripperName == 'Vacuume':
        open = customtkinter.CTkButton()
        #Close does not exist 
    else:
        close = customtkinter.CTkButton(gripper_frame, width=50, height=30)
        close.grid(column=1, row=1)


def fingerActivate():
    gripper_Select.pack_forget()
    #gripper.rowconfigure((0, 1), weight=1)
    #gripper.columnconfigure((0,1,2), weight=1)
    finger_label = customtkinter.CTkLabel(gripper_frame, width = 260, height=20, text='3 Finger Gripper', bg_color='grey')
    finger_label.pack()
    # create grid
    open_buttom = customtkinter.CTkButton(gripper_frame, text='OPEN', width=50, height=30)
    open_buttom.pack()
    #open_buttom.place(x=550, y=575)
    close_button = customtkinter.CTkButton(gripper_frame, text='CLOSE', width = 50, height = 30)
    close_button.pack()
    #close_button.place(x=600, y=575)

def ParallelActivate():
    gripper_Select.pack_forget()
    parallel_label = customtkinter.CTkLabel(gripper_frame, width = 260, height=20, text='Parallel Gripper', bg_color='grey')
    parallel_label.pack()

def VacuumeActivate():
    gripper_Select.pack_forget()
    vacuume_label = customtkinter.CTkLabel(gripper_frame, width = 260, height=20, text='Vacuume Gripper', bg_color='grey')
    vacuume_label.pack()

def option(choice):
    if choice == '3 Finger':
        fingerActivate()
    elif choice == 'Parallel Jaw':
        ParallelActivate()
    elif choice == 'Vacuume':
        VacuumeActivate()

def gripper():
    print('gripper')
    options = [
        'select',
        '3 Finger',
        'Parallel Jaw',
        'Vacuume'
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


app.mainloop()
vid.release()
