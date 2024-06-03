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

    grey_box = customtkinter.CTkFrame(app, width=150, height=30, fg_color="darkgrey")
    grey_box.place(x=200, y=620)
    text_label = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_label.place(x=225, y=620)

    #create joint movement sliders

   
        #disable joint lock, enable all axis, home robot, reset robot joint values. 

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="Activate", command=activate)
ActivateButton.place(x = 200, y = 620)
#create simulation box
simulation_box = customtkinter.CTkFrame(app, width=600, height=600, fg_color='grey')
simulation_box.place(x=10, y=10)


# Run the application
app.mainloop()