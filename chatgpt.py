import customtkinter

# Initialize customtkinter settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Main application setup
app = customtkinter.CTk()
app.title('Robot GUI')
app.geometry("1920x1080")  # Adjust the window size as needed

# Create a main frame for the sliders and place it at x=560
main_frame = customtkinter.CTkFrame(app, width=1200, height=500)
main_frame.place(x=560, y=50)

class Sliders(customtkinter.CTkFrame):

    def __init__(self, parent, joint_name, joint_coordinate, slider_position, target_position, plus, minus):
        super().__init__(master=parent)

        self.target_position = target_position
        self.plus = plus
        self.minus = minus

        # Configure grid layout
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)  # More space for slider
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Joint name label
        customtkinter.CTkLabel(self, text=joint_name).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        # Current position label
        self.target_label = customtkinter.CTkLabel(self, text=str(self.target_position))
        self.target_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        # Slider
        self.slider = customtkinter.CTkSlider(self, from_=0, to=100, command=self.update_from_slider)
        self.slider.set(slider_position)
        self.slider.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Joint coordinate label
        customtkinter.CTkLabel(self, text=joint_coordinate).grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        # Plus and minus buttons
        customtkinter.CTkButton(self, text='+', command=self.increase).grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        customtkinter.CTkButton(self, text='-', command=self.decrease).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        # Pack frame
        self.pack(expand=True, fill='both', padx=10, pady=10)

    def increase(self):
        self.target_position += self.plus
        self.update_display()

    def decrease(self):
        self.target_position -= self.minus
        self.update_display()

    def update_display(self):
        self.target_label.configure(text=str(self.target_position))
        self.slider.set(self.target_position)
        print(self.target_position)

    def update_from_slider(self, value):
        self.target_position = int(value)
        self.update_display()

# Create instances of the Sliders class within the main frame
Sliders(main_frame, 'Joint1R', '0', 50, 50, 5, 5)
Sliders(main_frame, 'Joint2R', '50', 50, 50, 5, 5)
Sliders(main_frame, 'Joint3R', '0', 50, 50, 5, 5)
Sliders(main_frame, 'Joint4R', '50', 50, 50, 5, 5)
Sliders(main_frame, 'Joint5R', '0', 50, 50, 5, 5)
Sliders(main_frame, 'Joint6R', '0', 50, 50, 5, 5)

# Start the main event loop
app.mainloop()
