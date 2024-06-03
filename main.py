import tk
import customtkinter

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color

# Create the main window
app = customtkinter.CTk()
app.title('Button')
app.geometry("1920x1080")

# Create a button
button = customtkinter.CTkButton(app, text="Click Me!")
button.pack(pady=20)

# Run the application
app.mainloop()