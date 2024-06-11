import tk
from tk import *
import customtkinter
import time



# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x780")


def program():
    title_box = customtkinter.CTkFrame(app, width=300, height=30, bg_color='grey')
    title_box.place(x=1000, y=10)
    grey_box = customtkinter.CTkScrollableFrame(app, width=650, height=600, bg_color='grey')
    grey_box.place(x=850, y=50)
    Program_label = customtkinter.CTkLabel(app, text = 'Program', bg_color = 'darkgrey')
    Program_label.place(x=1100, y=10)

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
    # time.sleep(3)#timer in place of robot connection and activation sequence

    #when connection is failed, add and else condition to the 'try'

    #when succesful connection achieved
    text_connected = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_connected.place(x=225, y=620)
    text_connecting.place_forget()
    app.update()
    program()
    
    #sliders(app, joint name, sliderposition, targetposition, plus/minus button effect)
    Sliders(app, 'Joint 1', 0, 0, 2, 2)
    Sliders(app, 'Joint 2', 0, 0, 5, 5)
    Sliders(app, 'Joint 3', 0, 0, 5, 5)
    Sliders(app, 'Joint 4', 0, 0, 5, 5)
    Sliders(app, 'Joint 5', 0, 0, 5, 5)
    Sliders(app, 'Joint 6', 0, 0, 5, 5)
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
class Sliders(customtkinter.CTkFrame):
    def __init__(self, parent, joint_name, slider_position, target_position, plus, minus): #joint_coordinate, 
        super().__init__(master=parent)
        self.target_position = target_position
        self.plus = plus
        self.minus = minus

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

        self.pack(padx=10, pady=10)
        self.grid_location(x=500, y=30)


#functinos to make the +/- buttons work and to correctly display the values
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




app.mainloop()