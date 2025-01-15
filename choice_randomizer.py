import tkinter as tk
import random
import time
import threading

# Uncommented lists for demonstration
places = [
    "Iloilo-Guimaras",
    "Siquijor-Dumaguete",
    "Bohol"
]

dates = [
    "May 15-17, 2025",
    "May 22-24, 2025"
]

def randomizer(list):
    return random.choice(list)

class Window(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        
        # Create a frame for the upper half
        upper_frame = tk.Frame(self, bg='black')
        upper_frame.pack(expand=True, fill='both')
        
        # Create a label with huge text
        self.huge_label = tk.Label(upper_frame, text="Huge Text Placeholder", font=("Helvetica", 24), anchor='center', fg='white', bg='black')
        self.huge_label.pack(expand=True, fill='both')
        
        # Create a frame for the lower half
        lower_frame = tk.Frame(self)
        lower_frame.pack(expand=True, fill='both')
        
        # Create a label with smaller text
        self.small_label = tk.Label(lower_frame, text="Small Text Placeholder", font=("Helvetica", 12), anchor='center', fg='white', bg='black')
        self.small_label.pack(expand=True, fill='both')

        # Create a button to trigger the randomizer
        self.randomize_button = tk.Button(lower_frame, text="Randomize", command=self.start_randomize, width=10, height=2, bg='blue', fg='black')
        self.randomize_button.pack(pady=20)

    def start_randomize(self):
        self.randomize_button.config(bg='green')
        threading.Thread(target=self.randomize).start()

    def randomize(self):
        countdown = 10
        while countdown > 0:
            for i in range(10):
                c_place = randomizer(places)
                c_date = randomizer(dates)
                self.huge_label.config(text=c_place)
                self.small_label.config(text=c_date)
                self.update_idletasks()
                time.sleep(0.2 * (1 / countdown))
            countdown -= 1
        self.randomize_button.config(bg='blue')

if __name__ == "__main__":
    window = Window("Randomizer", "400x300")
    window.mainloop()