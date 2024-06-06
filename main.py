import tk
from tk import *
import customtkinter
import time

#define joint variables FUTURE make this a class with joint min/max and speed values
class Joints ():
    Joint1R=0#base rotation
    Joint2R=0#shoulder
    Joint3R=0#elbow
    Joint4R=0#forearm rotation
    Joint5R=0#wrist rotation (up down)
    Joint6R=0#tool rotation (rotating tool)

# System appearance and config
class app(customtkinter.CTk):
    def __init__(self, title, size):
        
        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        #self.minsize(size[0], size[1])
        #self.minsize(1500,780)

        #widgets
        #self.activate = Activate(self)
        self.sim = Sim(self)
        #self.controll = Controll(self)
        #self.program = Program(self)




        self.mainloop()


class Sim(customtkinter.frame):
    def __init__(self, parent):
        super().__init__(parent)



app('Robot GUI', (1920,780))
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
#app = customtkinter.CTk()
#app.title('Robot GUI')
#app.geometry("1920x780")


def program():
    title_box = customtkinter.CTkFrame(app, width=300, height=30, bg_color='grey')
    title_box.place(x=1000, y=10)
    grey_box = customtkinter.CTkScrollableFrame(app, width=650, height=600, bg_color='lightgrey')
    grey_box.place(x=850, y=50)

def connect():
    ActivateButton.pack_forget()  # Hide the button
    #replace button with shaded textbox
    grey_box = customtkinter.CTkFrame(app, width=150, height=30, fg_color="darkgrey")
    grey_box.place(x=200, y=620)
    grey_box.pack
#say connecting to robot... in orange or blue
    text_connecting = customtkinter.CTkLabel(app, text="Robot Connecting...", text_color="darkorange", bg_color="darkgrey")
    text_connecting.place(x=225, y=620)
    app.update()
    time.sleep(3)#timer in place of robot connection and activation sequence

    #when connection is failed, add and else condition to the 'try'

    #when succesful connection achieved
    text_connected = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_connected.place(x=225, y=620)
    text_connecting.place_forget()
    app.update()
    sliders()
    program()
    #create joint movement sliders
        #disable joint lock, enable all axis, home robot, reset robot joint values.

def disconnect(text_connected):
    #ActivateButton = customtkinter.CTkButton(app, text="connect", command=connect)
    #ActivateButton.place(x = 200, y = 620)
    text_connected.place_forget()

#def resetJoints():
    #baseX=0        

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="connect", command=connect)
ActivateButton.place(x = 200, y = 620)

DisconnectButton = customtkinter.CTkButton(app, width=75, text='(/)', command=disconnect)
DisconnectButton.place(x=500, y=620)
#ResetJointsButton = customtkinter.CTkButton(app, text='reset joints', comand=resetJoints)
#create simulation joint
simulation_joint = customtkinter.CTkFrame(app, width=550, height=600, fg_color='grey')
simulation_joint.place(x=10, y=10)
#create slider joint
slider_joint = customtkinter.CTkFrame(app, width=250, height=600, fg_color='grey')
slider_joint.place(x=570, y=10)


 
 # Function to update slider percentage
def update_slider_label(slider, label):
    value = round(slider.get() - 50, 1)
    label.configure(text=f"{value}%")
 #makes the sliders and titles, also displays robot rotation degrees for each joint
def sliders():
    # Slider 1
    #change sliders so they display the actual position from the robot joints as defined above, 
    #have the sliders adjust the target position of the robot joints
    #when the 'home robot' button is pressed, set all robot joints back to 0 and reset sliders to 0
    #have the sliders locked until homing is complete (have a 'homing' house image display over the sliders to hide them till done homing)

    joint1_name = customtkinter.CTkLabel(app, text="Joint 1", bg_color='grey',font=("Arial", 15))
    joint1_name.place(x=600, y=50)
    #joint1_plus = customtkinter.CTkButton(app, text='+', command= jointX+='5')
    joint1 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint1, joint1_percent))
    joint1.place(x=600, y=70)
    joint1_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint1_percent.place(x=770, y=35)
    app.update()
    

    joint2_name = customtkinter.CTkLabel(app, text="Joint 2", bg_color='grey', font=("Arial", 15))
    joint2_name.place(x=600, y=150)
    joint2 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint2, joint2_percent))
    joint2.place(x=600, y=170)
    joint2_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint2_percent.place(x=770, y=135)

    joint3_name = customtkinter.CTkLabel(app, text="Joint 3", bg_color='grey', font=("Arial", 15))
    joint3_name.place(x=600, y=250)
    joint3 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint3, joint3_percent))
    joint3.place(x=600, y=270)
    joint3_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint3_percent.place(x=770, y=235)

    joint4_name = customtkinter.CTkLabel(app, text="Joint 4", bg_color='grey', font=("Arial", 15))
    joint4_name.place(x=600, y=350)
    joint4 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint4, joint4_percent))
    joint4.place(x=600, y=370)
    joint4_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint4_percent.place(x=770, y=330)

    joint5_name = customtkinter.CTkLabel(app, text="Joint 5", bg_color='grey', font=("Arial", 15))
    joint5_name.place(x=600, y=450)
    joint5 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint5, joint5_percent))
    joint5.place(x=600, y=470)
    joint5_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint5_percent.place(x=770, y=430)

    joint6_name = customtkinter.CTkLabel(app, text="Joint 6", bg_color='grey', font=("Arial", 15))
    joint6_name.place(x=600, y=550)
    joint6 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(joint6, joint6_percent))
    joint6.place(x=600, y=570)
    joint6_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    joint6_percent.place(x=770, y=530)

# Run the application
app.mainloop()