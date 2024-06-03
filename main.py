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

def activate():
   T = tk.Text(app, height=2, width=30)
   T.pack()
   T.insert(tk.END, "Just a text Widget\nin two lines\n")
        #disable joint lock, enable all axis, home robot, reset robot joint values.

        #add text that says 'robot connected'

    

# Create a button
ActivateButton = customtkinter.CTkButton(app, text="Activate", command = activate) #command = ActivateButton.destroy
ActivateButton.place(x = 100, y = 100)

# Run the application
app.mainloop()