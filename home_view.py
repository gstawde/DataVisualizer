import os
from tkinter import *
from tkinter import ttk

class HomeView:
    
    def __init__(self, root):
        
        root.title("New York Lottery Analysis Home View")
        root.geometry('500x200')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # make a frame for the GUI
        self.frame = ttk.Frame(root, padding = "10 10 10 10")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # weight column to expand with the window
        self.frame.columnconfigure(0, weight=1)

        label = ttk.Label(self.frame, text=str('New York Lottery Analysis Platform!'))
        label.grid(column=0, row=0, sticky=(N, W, E, S))

        # Powerball Window
        self.button_new_window = ttk.Button(self.frame, text="POWERBALL", command=self.powerball_window)
        self.button_new_window.grid(column=0, row=1, sticky=(N, W, E, S))

        # Mega Millions Window
        self.button_new_window = ttk.Button(self.frame, text="MEGA MILLIONS", command=self.mega_millions_window)
        self.button_new_window.grid(column=0, row=2, sticky=(N, W, E, S))

        # add a button to close the app
        self.button_close = ttk.Button(self.frame,
                                          text="EXIT", command=root.destroy)
        self.button_close.grid(column=0, row=3, sticky=(N, W, E, S))
        

    # POWERBALL Window
    def powerball_window(self):
        os.system('python3 powerball.py')

    # MEGA MILLIONS WINDOW
    def mega_millions_window(self):
        os.system('python3 mega_millions.py')

        


root = Tk()

HomeView(root)

root.mainloop()