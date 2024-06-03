import tk
import customtkinter

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x980")

def activate():
    print('i was called')
    ActivateButton.pack_forget()  # Hide the button
    #replace button with shaded textbox
    grey_box = customtkinter.CTkFrame(app, width=150, height=30, fg_color="darkgrey")
    grey_box.place(x=200, y=620)

    #when succesful connection achieved
    text_label = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_label.place(x=225, y=620)
    sliders()
    #create joint movement sliders
        #disable joint lock, enable all axis, home robot, reset robot joint values.
        

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="Activate", command=activate)
ActivateButton.place(x = 200, y = 620)
#create simulation box
simulation_box = customtkinter.CTkFrame(app, width=550, height=600, fg_color='grey')
simulation_box.place(x=10, y=10)
#create slider box
slider_box = customtkinter.CTkFrame(app, width=250, height=600, fg_color='grey')
slider_box.place(x=570, y=10)


 
def sliders():
    box1_name = customtkinter.CTkLabel(app, text="Joint 1", bg_color='grey',font=("Arial", 10))
    box1_name.place(x=700, y=80)
    box1 = customtkinter.CTkSlider(app, from_=0, to=200)
    box1.place(x=600, y=100)
    box1.pack
    box2 = customtkinter.CTkSlider(app, from_=0, to=200)
    box2.place(x=600, y=200)
    box2.pack
    box3 = customtkinter.CTkSlider(app, from_=0, to=200)
    box3.place(x=600, y=300)
    box3.pack






# Run the application
app.mainloop()