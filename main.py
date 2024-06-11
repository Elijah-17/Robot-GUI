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

allSLiders = []

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

    #sliders(app, joint name, sliderposition, targetposition, plus/minus button effet
    allSliders = [
    Sliders(slider_frame, 'Joint 1', 0, 0, 2, 2),
    Sliders(slider_frame, 'Joint 2', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 3', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 4', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 5', 0, 0, 5, 5),
    Sliders(slider_frame, 'Joint 6', 0, 0, 5, 5)
    ]
    #create joint movement sliders
        #disable joint lock, enable all axis, home robot, reset robot joint values.

    

#create frames for portions of window
webCam_frame = customtkinter.CTkFrame(app, width=550, height=600)
webCam_frame.place(x=10, y=10)
program_frame = customtkinter.CTkFrame(app, width=550, height=600)
program_frame.place(x=830, y=10)
#slider frame changes size when the sliders are activated, idk why tbh.
slider_frame = customtkinter.CTkFrame(app, width=250, height=500)
slider_frame.place(x=570, y=10)


# Create a button
ActivateButton = customtkinter.CTkButton(app, text="connect", command=connect)
ActivateButton.place(x = 200, y = 620)

# Home_Button = customtkinter.CTkButton(slider_frame, width=75, text='U^', command=reset_all_sLiders)
# Home_Button.place(x=500, y=620)
#ResetJointsButton = customtkinter.CTkButton(app, text='reset joints', comand=resetJoints)

 
 # Function to update slider percentage
class Sliders(customtkinter.CTkFrame):
    def __init__(self, parent, joint_name, slider_position, target_position, plus, minus): #joint_coordinate, 
        super().__init__(master=parent)
        self.target_position = target_position
        self.plus = plus
        self.minus = minus
        self.original_position = target_position


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
def reset_all_sLiders():
    for sliders in allSLiders:
        sliders.home()



Home_Button = customtkinter.CTkButton(slider_frame, width=75, text='U^', command=reset_all_sLiders)
Home_Button.place(x=500, y=620)
app.mainloop()