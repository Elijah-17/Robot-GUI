import tk
import customtkinter
import time

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x980")

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
    #time.sleep(3)#timer in place of robot connection and activation sequence

    #when connection is failed, add and else condition to the 'try'

    #when succesful connection achieved
    text_label = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_label.place(x=225, y=620)
    text_connecting.place_forget()
    app.update()

    sliders()
    #create joint movement sliders
        #disable joint lock, enable all axis, home robot, reset robot joint values.
        

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="connect", command=connect)
ActivateButton.place(x = 200, y = 620)
#create simulation box
simulation_box = customtkinter.CTkFrame(app, width=550, height=600, fg_color='grey')
simulation_box.place(x=10, y=10)
#create slider box
slider_box = customtkinter.CTkFrame(app, width=250, height=600, fg_color='grey')
slider_box.place(x=570, y=10)


 
 # Function to update slider percentage
def update_slider_label(slider, label):
    value = round(slider.get() - 50, 1)
    label.configure(text=f"{value}%")
 #makes the sliders and titles, also displays robot rotation degrees for each joint
def sliders():
    # Slider 1
    box1_name = customtkinter.CTkLabel(app, text="Joint 1", bg_color='grey', font=("Arial", 10))
    box1_name.place(x=600, y=80)
    box1 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(box1, box1_percent))
    box1.place(x=600, y=100)
    box1_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box1_percent.place(x=600, y=60)

    box2_name = customtkinter.CTkLabel(app, text="Joint 2", bg_color='grey', font=("Arial", 10))
    box2_name.place(x=600, y=180)
    box2 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(box2, box2_percent))
    box2.place(x=600, y=200)
    box2_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box2_percent.place(x=600, y=160)

    box3_name = customtkinter.CTkLabel(app, text="Joint 3", bg_color='grey', font=("Arial", 10))
    box3_name.place(x=600, y=280)
    box3 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(box3, box3_percent))
    box3.place(x=600, y=300)
    box3_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box3_percent.place(x=600, y=260)

    box4_name = customtkinter.CTkLabel(app, text="Joint 4", bg_color='grey', font=("Arial", 10))
    box4_name.place(x=600, y=380)
    box4 = customtkinter.CTkSlider(app, from_=0, to=100, command=lambda value: update_slider_label(box4, box4_percent))
    box4.place(x=600, y=400)
    box4_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box4_percent.place(x=600, y=360)

    box5_name = customtkinter.CTkLabel(app, text="Joint 5", bg_color='grey', font=("Arial", 10))
    box5_name.place(x=600, y=480)
    box5 = customtkinter.CTkSlider(app, from_=-50, to=50, command=lambda value: update_slider_label(box5, box5_percent))
    box5.place(x=600, y=500)
    box5_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box5_percent.place(x=600, y=460)

    box6_name = customtkinter.CTkLabel(app, text="Joint 6", bg_color='grey', font=("Arial", 10))
    box6_name.place(x=600, y=580)
    box6 = customtkinter.CTkSlider(app, from_=-50, to=50, command=lambda value: update_slider_label(box6, box6_percent))
    box6.place(x=600, y=600)
    box6_percent = customtkinter.CTkLabel(app, text="0.0%", bg_color='grey')
    box6_percent.place(x=600, y=560)






# Run the application
app.mainloop()