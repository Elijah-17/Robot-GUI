import tk
from tk import *
import customtkinter
import time
# System appearance and config
class app(customtkinter.CTk):
    def __init__(self, title, size):
        
        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        #self.minsize(size[0], size[1])
        #self.minsize(1500,780)

        #widgets
        #self.activate = Activate(self)
        self.sliders = Sliders(self)
        #self.controll = Controll(self)
        #self.program = Program(self)
        self.mainloop()


class Activate(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        customtkinter.CTkLabel(self, background= 'lightgrey').pack(fill='both')
        #self.place(x=10, y=10, relwidth = 0.3, relheight = 1)

    def create_widgets(self):
        # Create a button
        activate_Button = customtkinter.CTkButton(self, text = "connect", command=connect)
        activate_Button.place(x = 200, y = 620)



class Sliders(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def create_widgets(self):
        title_box = customtkinter.CTkFrame(app, width=300, height=30, bg_color='grey')
        title_box.place(x=1000, y=10)
        grey_box = customtkinter.CTkScrollableFrame(app, width=650, height=600, bg_color='lightgrey')
        grey_box.place(x=850, y=50)
    def create_layout(self):
        self.columnconfigure((0,))

app('Robot GUI', (1920,780))
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')