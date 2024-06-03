import tk
import customtkinter

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x1080")

class activate(self):
    try
        #disable joint lock, enable all axis, home robot, reset robot joint values.
        
    

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="Activate", command = activate, command = ActivateButton.destroy)
ActivateButton.place(x = 100, y = 100)
    #activate robot joints and diable joint lock

# Run the application
app.mainloop()