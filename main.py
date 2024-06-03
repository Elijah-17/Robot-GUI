import tkinter
import customtkinter

# System appearance and config
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Function to change button color
def change_button_color():
    button.config(bg="green")

# Create the main window
app = customtkinter.CTk()
app.title('Button')
app.geometry("300x200")

# Create a button
button = customtkinter.CTkButton(app, text="Click Me!", command=change_button_color)
button.pack(pady=20)

# Run the application
app.mainloop()