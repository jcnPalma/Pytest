import tkinter as tk

class Window(tk.Tk):
    def __init__(self, title="Hello, World!", windowSize="300x200"):
        tk.Tk.__init__(self)
        self.title(title)
        self.geometry(windowSize)
        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack()