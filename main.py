import tk
import customtkinter

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("920x1080")

def activate():
    print('i was called')
    ActivateButton.pack_forget()  # Hide the button

    grey_box = customtkinter.CTkFrame(app, width=150, height=30, fg_color="darkgrey")
    grey_box.place(x=100, y=100)
    text_label = customtkinter.CTkLabel(app, text="Robot Connected", text_color="green", bg_color="darkgrey")
    text_label.place(x=125, y=100)
   
        #disable joint lock, enable all axis, home robot, reset robot joint values. 

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="Activate", command=activate)
ActivateButton.place(x = 100, y = 100)



# Run the application
app.mainloop()