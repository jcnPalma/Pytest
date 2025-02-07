import tkinter as tk
import threading
import random
import time

gl_accs = ["DFAC T", "DFAC N", "DTAC T", "DTAC N"]
entities = ["UNITED LABORATORIES, INC. (1000)", "UL HEALTH GROUP, INC. (2000)", 
            "UNILAB, INC. (3100)", "RITEMED PHILS, INC. (3200)", 
            "UL SKIN SCIENCES, INC. (3500)", "AMHERST NUTRACEUTICALS, INC. (4000)", 
            "ASIAN ANTIBIOTICS, INC. (4010)", "AMHERST PARENTERALS, INC. (4020)", 
            "AMHERST LABORATORIES, INC (4030)", "BELMONT SOFTGEL PHARMA CO (4040)", 
            "BEAUTÉ ET SCIENCE LABORAT (4600)", "WESTMONT PHARMACEUTICALS (5000)", 
            "UAP, INC. (5010)", "THERAPHARMA, INC. (5020)", "PEDIATRICA, INC. (5030)", 
            "BIOMEDIS, INC. (5040)", "MEDICHEM PHARMACEUTICALS (5050)", "L. R. IMPERIAL, INC. (5060)", 
            "BIOFEMME, INC. (5070)", "BIO ONCOLOGY, INC. (5080)", "UH PHARMA, INC. (5090)", 
            "INNOVITELLE INC. (5700)", "UNILAB ACTIVE HEALTH, INC (7000)"]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
years = [20, 21, 22, 23]


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
        self.entity_label = tk.Label(upper_frame, wraplength=500, height=4,text="Entity", font=("Helvetica", 20), anchor='center', fg='white', bg='black')
        self.entity_label.pack(expand=True, fill='both')
        
        # Create a frame for the lower half
        lower_frame = tk.Frame(self)
        lower_frame.pack(expand=True, fill='both')

        # Create a frame for left half
        left_frame = tk.Frame(lower_frame, bg='blue')
        left_frame.pack(side=tk.LEFT, expand=True, fill='both')

        # Create a frame for right half
        right_frame = tk.Frame(lower_frame, bg='red')
        right_frame.pack(side=tk.RIGHT, expand=True, fill='both')

        # Create a label with smaller text in the left frame
        self.gl_account_label = tk.Label(left_frame, text="GL Account", font=("Helvetica", 12), anchor='center', fg='white', bg='black')
        self.gl_account_label.pack(expand=True, fill='both')

        # Create a label with smaller text in the right frame
        self.date_label = tk.Label(right_frame, text="Date", font=("Helvetica", 12), anchor='center', fg='white', bg='black')
        self.date_label.pack(expand=True, fill='both')

        # Create a frame for button
        button_frame = tk.Frame(self, bg='black') 
        button_frame.pack(expand=True, fill='both')

        # Create a button to trigger the randomizer
        self.randomize_button = tk.Button(button_frame, text="Randomize", command=self.start_randomize, width=10, height=2, bg='blue', fg='black')
        self.randomize_button.pack(pady=20)

    def start_randomize(self):
        self.randomize_button.config(bg='green')
        threading.Thread(target=self.randomize).start()

    def randomize(self):
        countdown = 10
        while countdown > 0:
            for i in range(10):
                c_entity = randomizer(entities)
                c_gl_acc = randomizer(gl_accs)
                c_month = randomizer(months)
                c_year = randomizer(years)
                self.entity_label.config(text=c_entity)
                self.gl_account_label.config(text=c_gl_acc)
                self.date_label.config(text=c_month + " " + str(c_year))
                self.update_idletasks()
                time.sleep(0.2 * (1 / countdown))
            countdown -= 1
        self.randomize_button.config(bg='blue')

if __name__ == "__main__":
    window = Window("Randomizer", "600x400")
    window.mainloop()