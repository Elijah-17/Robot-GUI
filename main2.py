import tk
from tk import *
import customtkinter
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
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x780")


def increase(targetposition, plus):
        targetposition += plus
        print(targetposition)

def decrease(targetposition, minus):
        targetposition -= minus
        print(targetposition)

class Sliders(customtkinter.CTkFrame):

    def __init__(self, parent, joint_name, joint_choordinate, slider_position, target_position, plus, minus):
        super().__init__(master = parent)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0,1,2), weight =1)
        customtkinter.CTkLabel(self, text = joint_name).grid(row=0, column=0)
        customtkinter.CTkSlider(self, from_=0, to=100).grid(row=1, column=1)
        customtkinter.CTkLabel(self, text = joint_choordinate).grid(row=0, column =2)
        customtkinter.CTkButton(self, text = '+', command= increase).grid(row=1, column =2)
        customtkinter.CTkButton(self, text = '-', command= decrease).grid(row=1, column =0)


        self.pack(expand = True, fill='both', padx=10, pady=10)
        return(target_position, plus, minus)

#app('Robot GUI', (1920,780))
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
#sliders(app, joint name, joint choordinate, sliderposition, targetposition, )
Sliders(app, 'Joint1R', '0', '0', '50', '5', '5')
Sliders(app, 'Joint2R', '50', '0', '50', '5', '5')
Sliders(app, 'Joint3R', '0', '0', '50', '5', '5')
Sliders(app, 'Joint4R', '50', '0', '50', '5', '5')
Sliders(app, 'Joint5R', '0', '0', '50', '5', '5')
Sliders(app, 'Joint6R', '0', '0', '50', '5', '5')



app.mainloop()