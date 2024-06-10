import customtkinter
import tk
from tk import *
import time


# System appearance and config
# class app(customtkinter.CTk):
#     def __init__(self, title, size):

#         #main setup
#         super().__init__()
#         self.title(title)
#         self.geometry(f'{size[0]}x{size[1]}')
#         #self.minsize(size[0], size[1])
#         self.minsize(900,780)


#        self.mainloop()

# Initialize customtkinter settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Main application setup
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x780")



class Sliders(customtkinter.CTkFrame):
    def __init__(self, parent, joint_name, slider_position, target_position, plus, minus): #joint_coordinate, 
        super().__init__(master=parent)
        self.target_position = target_position
        self.plus = plus
        self.minus = minus

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0,1,2, 3, 4), weight=1)

        customtkinter.CTkLabel(self, text=joint_name).grid(row=0, column=0)
        self.slider = customtkinter.CTkSlider(self, from_=-50, to=50, command=self.update_from_slider)
        self.slider.set(slider_position)
        self.slider.grid(row=1, column=2)
       
        #when using robotic arm, use line 31 and comment out 32 & 33.
        #customtkinter.CTkLabel(self, text=joint_coordinate).grid(row=0, column=4)
        self.target_label = customtkinter.CTkLabel(self, text=str(self.target_position))
        self.target_label.grid(row=0, column=4)

        customtkinter.CTkButton(self, text='+', command=self.increase).grid(row=1, column=3)
        customtkinter.CTkButton(self, text='-', command=self.decrease).grid(row=1, column=1)

        self.pack(expand=True, fill='both', padx=10, pady=10)

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
Sliders(app, 'Joint1R', 0, 0, 5, 5)
Sliders(app, 'Joint2R', 0, 0, 5, 5)
Sliders(app, 'Joint3R', 0, 0, 5, 5)
Sliders(app, 'Joint4R', 0, 0, 5, 5)
Sliders(app, 'Joint5R', 0, 0, 5, 5)
Sliders(app, 'Joint6R', 0, 0, 5, 5)



app.mainloop()
