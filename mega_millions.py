import csv
import os
from tkinter import *
from tkinter import ttk


filepath = 'Lottery_Mega_Millions_Winning_Numbers__Beginning_2002-2.csv'
file = open(filepath)
file_reader = csv.reader(file)

data = list(file_reader)
del(data[0])

# Access Data
list_of_dates = []
list_of_mega_millions = []
list_of_winning_numbers = []

for x in list(range(0,len(data))):
    list_of_dates.append(data[x][0])
    list_of_mega_millions.append(data[x][2])
    split_vals = data[x][1].split()
    for i in range(0, len(split_vals)):
        list_of_winning_numbers.append(split_vals[i])
# data is in 4 columns: 'Draw Date', 'Winning Numbers', 'Mega Ball', 'Multiplier'



class Powerball:
    
    def __init__(self, root):
        
        root.title("Mega Millions")
        root.geometry('700x500')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # make a frame for the GUI
        self.frame = ttk.Frame(root, padding = "10 10 10 10")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # weight column to expand with the window
        self.frame.columnconfigure(0, weight=1)

        # Window Title and usage instructions
        self.label = ttk.Label(self.frame, text=str('Mega Millions Data'))
        self.label.grid(column=0, row=0, sticky=(N, W, E, S))
        self.how_to = ttk.Label(self.frame, text=str('Scroll through the list of dates below. Select any date,\nthen click the \'Get Data\' button in order to view that date\'s\Mega Millions information.'))
        self.how_to.grid(column=0, row=1, sticky=(N, W, E, S))


        # Mega Millions Dates
        self.listbox1 = Listbox(root)
        for x, y in enumerate(list_of_dates):
            self.listbox1.insert(x,y)
        self.listbox1.grid(column=0, row=2, sticky=(N, W, E, S))

        # Labels that will hold data based on selected Date in listbox
        self.date = ttk.Label(self.frame, text=str('Draw Date'))
        self.date.grid(column=0, row=3, sticky=(N, W, E, S))
        self.winning_numbers = ttk.Label(self.frame, text=str('Winning Numbers'))
        self.winning_numbers.grid(column=0, row=4, sticky=(N, W, E, S))
        self.mega_ball = ttk.Label(self.frame, text=str('Mega Ball'))
        self.mega_ball.grid(column=0, row=5, sticky=(N, W, E, S))
        self.multiplier = ttk.Label(self.frame, text=str('Multiplier'))
        self.multiplier.grid(column=0, row=6, sticky=(N, W, E, S))

        # Updates where cursor is in listbox
        self.update_button = ttk.Button(self.frame, text="GET DATA", command=self.update)
        self.update_button.grid(column=0, row=7, sticky=(N, W, E, S))

        # Most common mega million number
        self.most_common_mega_million = ttk.Label(self.frame, text=str('Most Common Mega Million Number'))
        self.most_common_mega_million.grid(column=0, row=8, sticky=(N, W, E, S))
        self.most_common = ttk.Button(self.frame, text="MOST COMMON MEGA MILLION NUMBER", command=self.update_most_common_mega_million)
        self.most_common.grid(column=0, row=9, sticky=(N, W, E, S))

        # Frequency Data Window
        self.button_new_window = ttk.Button(self.frame, text="Common Winning Numbers", command=self.megamillions_freq_window)
        self.button_new_window.grid(column=0, row=10, sticky=(N, W, E, S))

        # Add a button to close the app
        self.button_close = ttk.Button(self.frame, text="EXIT", command=root.destroy)
        self.button_close.grid(column=1, row=0, sticky=(N, W, E, S))

    # Mega Millions Frequency Graph Window
    def megamillions_freq_window(self):
        os.system('python3 megamillions_frequencies.py')

    # Updates the label to hold the most common value over the years for the mega million
    def update_most_common_mega_million(self):
        count = 0
        most_common = list_of_mega_millions[0]
        for i in list_of_mega_millions:
            curr_frequency = list_of_mega_millions.count(i)
            if(curr_frequency> count):
                count = curr_frequency
                most_common = i
        self.most_common_mega_million.config(text="Most Common Mega Million Number: " + str(most_common))

    # Updates the labels for data corresponding to the date in the list the user has selected
    def update(self):
        index = self.listbox1.curselection()[0]
        self.date.config(text='Date: ' + data[index][0])
        self.winning_numbers.config(text='Winning numbers: ' + data[index][1])
        self.mega_ball.config(text='Mega Ball: ' + data[index][2])
        self.multiplier.config(text='Multiplier: ' + data[index][3])
        return None
      


root = Tk()

Powerball(root)

root.mainloop()