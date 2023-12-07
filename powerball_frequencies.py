import csv
import os
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np

filepath = 'Lottery_Powerball_Winning_Numbers__Beginning_2010-2.csv'
file = open(filepath)
file_reader = csv.reader(file)

data = list(file_reader)
del(data[0])

# # Access Data
list_of_winning_numbers = []
list_of_frequencies = []

for x in list(range(0,len(data))):
    split_vals = data[x][1].split()
    for i in range(0, len(split_vals)):
        list_of_winning_numbers.append(split_vals[i])

# Create list of frequencies of winning numbers
for i in list_of_winning_numbers:
    curr_frequency = list_of_winning_numbers.count(i)
    tup = (i, curr_frequency)
    if (len(list_of_frequencies) == 0 or tup[0] not in list_of_frequencies[0]):
        list_of_frequencies.append(tup)
val = []
fre = []
for item in list_of_frequencies:
    val.append(item[0])
    fre.append(item[1])

fig, ax = plt.subplots(figsize = (12, 8))
ax.grid()
plt.setp(ax.get_xticklabels(), rotation = 75)


plt.bar(val, fre)

plt.show()



root = Tk()

root.mainloop()

# © 2023 Gargi Tawde DataVisualizer. All Rights Reserved.