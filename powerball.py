import csv
import os
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from tkmacosx import Button
import tkinter.font as tkFont

filepath = 'Lottery_Powerball_Winning_Numbers__Beginning_2010-2.csv'
file = open(filepath)
file_reader = csv.reader(file)

data = list(file_reader)
del(data[0])

# Access Data
list_of_dates = []
list_of_winning_numbers = []

for x in list(range(0,len(data))):
    list_of_dates.append(data[x][0])
    split_vals = data[x][1].split()
    for i in range(0, len(split_vals)):
        list_of_winning_numbers.append(split_vals[i])

# data is in 3 columns: date, numbers, multiplier

class Powerball:
    
    def __init__(self, root):
        
        root.title("Powerball")
        root.geometry('700x450')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # make a frame for the GUI
        self.frame = ttk.Frame(root, padding = "10 10 10 10")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # weight column to expand with the window
        self.frame.columnconfigure(0, weight=1)

        # Window Title and usage instructions
        self.label = ttk.Label(self.frame, text=str('Powerball Data'), font=('Times New Roman', 26, 'bold'))
        self.label.grid(column=0, row=0, sticky=(N, W, E, S))
        self.how_to = ttk.Label(self.frame, text=str('Scroll through the list of dates below. Select any date,then click the \'Get Data\' button\nin order to view that date\'s Powerball information.\n'))
        self.how_to.grid(column=0, row=1, sticky=(N, W, E, S))

        # Powerball Dates
        self.listbox1 = Listbox(root)
        for x, y in enumerate(list_of_dates):
            self.listbox1.insert(x,y)
        self.listbox1.grid(column=0, row=2, sticky=(N, W, E, S))

        # Updates where cursor is in listbox
        self.update_button = Button(self.frame, text="GET DATA", bg='orange', fg='white', command=self.update)
        self.update_button.grid(column=0, row=6, sticky=(N, W, E, S))

        # Labels that will hold data based on selected Date in listbox
        self.date = ttk.Label(self.frame, text=str('Draw Date'))
        self.date.grid(column=0, row=3, sticky=(N, W, E, S))
        self.winning_numbers = ttk.Label(self.frame, text=str('Winning Numbers'))
        self.winning_numbers.grid(column=0, row=4, sticky=(N, W, E, S))
        self.multiplier = ttk.Label(self.frame, text=str('Multiplier'))
        self.multiplier.grid(column=0, row=5, sticky=(N, W, E, S))

        # Frequency Data Window
        self.button_new_window = Button(self.frame, text="Common Winning Numbers", bg='green', fg='white', command=self.powerball_freq_window)
        self.button_new_window.grid(column=0, row=12, sticky=(N, W, E, S))

        # Add a button to close the app
        self.button_close = Button(self.frame, text="EXIT", bg='red', fg='white', command=root.destroy)
        self.button_close.grid(column=2, row=0, sticky=(N, W, E, S))

    # Powerball Frequency Graph Window
    def powerball_freq_window(self):
        os.system('python3 powerball_frequencies.py')

    # Updates the labels for data corresponding to the date in the list the user has selected
    def update(self):
        index = self.listbox1.curselection()[0]
        self.date.config(text='Date: ' + data[index][0])
        self.winning_numbers.config(text='Winning numbers: ' + data[index][1])
        self.multiplier.config(text='Multiplier: ' + data[index][2])
        return None

        


root = Tk()

Powerball(root)

root.mainloop()


# © 2023 Gargi Tawde DataVisualizer. All Rights Reserved.