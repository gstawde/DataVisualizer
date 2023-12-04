import csv
from tkinter import *
from tkinter import ttk


filepath = '/Users/gargitawde/Desktop/sjsu/Fall2023/CS 122/FinalProject/DataVisualizer/Lottery_Powerball_Winning_Numbers__Beginning_2010-2.csv'
File = open(filepath)
Reader = csv.reader(File)

Data = list(Reader)

# Access Data
# list_of_dates = []
# for x in list(range(0,len(Data))):
#     list_of_dates.append(Data[x][0])


class HomeView:
    
    def __init__(self, root):
        
        root.title("New York Lottery Analysis Home View")
        root.geometry('280x300')

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


    # POWERBALL Window
    def powerball_window(self):
        win = Toplevel()
        win.wm_title('Powerball Window')
        
        label = ttk.Label(win, text="New widgets go here")
        label.grid(row=0, column=0)

        self.button_close = ttk.Button(win,
        text="Close", command=win.destroy)
        self.button_close.grid(column=0, row=5, sticky=(N, W, E, S))

    # MEGA MILLIONS WINDOW
    def mega_millions_window(self):
        win = Toplevel()
        win.wm_title('Mega Millions Window')
        
        label = ttk.Label(win, text="New widgets go here")
        label.grid(row=0, column=0)

        self.button_close = ttk.Button(win,
        text="Close", command=win.destroy)
        self.button_close.grid(column=0, row=5, sticky=(N, W, E, S))




root = Tk()

HomeView(root)

root.mainloop()