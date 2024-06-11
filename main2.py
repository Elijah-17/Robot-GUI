import customtkinter
import tk
from tk import *
import time


# System appearance and config
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x980")

# Initialize customtkinter settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


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

        customtkinter.CTkButton(self, text='+', command=self.increase).grid(row=1, column=2)
        customtkinter.CTkButton(self, text='-', command=self.decrease).grid(row=1, column=0)

        self.pack(expand=True, fill='both', padx=10, pady=10)
        self.grid_location(x=570, y=10)
        self.grid_size

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

#sliders(app, joint name, sliderposition, targetposition, plus and minus button effect)
Sliders(app, 'Joint 1', 0, 0, 5, 5)
Sliders(app, 'Joint 2', 0, 0, 5, 5)
Sliders(app, 'Joint 3', 0, 0, 5, 5)
Sliders(app, 'Joint 4', 0, 0, 5, 5)
Sliders(app, 'Joint 5', 0, 0, 5, 5)
Sliders(app, 'Joint 6', 0, 0, 5, 5)



app.mainloop()
