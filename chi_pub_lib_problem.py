# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

# Dividing up the data into a readable list
lib_data = []
file = open("chilib_visitors_2016", "r")
reader = csv.reader(file, delimiter = '\t')
for line in reader:
    lib_data.append(line)
print(lib_data)

#------Sorting-------
headers = lib_data[0][1:-1]
print(headers)
lib_data = lib_data[1:]

#Total visitors per month for all libraries
total_list = []
for month in range(12):
    total_visitors = 0
    for i in range(len(lib_data)):
        total_visitors += int(lib_data[i][month + 1])
    total_list.append(total_visitors)
    #print("Total number of visitors: ", month, ": ", total_visitors)

#Sorting the top three libraries
lib_data.sort(key = itemgetter(-1))
for i in range(len(lib_data)):
    lib_data[i][-1] = int(lib_data[i][-1])

lib_data.sort(key = itemgetter(-1))
print("Top three most visited libraries: ", end = "")
print(lib_data[-3:])


#-----Graphing------
x = np.arange(12)#lib_data[0][1:-1] # Each of the months and the YTD
print(x)
y_1 = lib_data[-1][1:-1] #Harold Washington Library
print(y_1)
y_2 = lib_data[-2][1:-1] #Sulzer library
print(y_2)
y_3 = lib_data[-3][1:-1] #Chinatown library
print(y_3)
y_tot = total_list #total for each month for every library combined

#size of screen
plt.figure(figsize=[8,5], tight_layout=True)

#plotting
line1, = plt.plot(x,y_1)
line2, = plt.plot(x,y_2)
line3, = plt.plot(x,y_3)
line_tot, = plt.plot(x, y_tot)

line1.set_linewidth(3) # pixels
line1.set_color('darkgreen') # set color of line
line1.set_linestyle('-')
line1.set_marker('8') # look up under plt.plot or set_properties
line1.set_markersize(5)

line2.set_linewidth(3) # pixels
line2.set_color('red') # set color of line
line2.set_linestyle('-')
line2.set_marker('8') # look up under plt.plot or set_properties
line2.set_markersize(5)

line3.set_linewidth(3) # pixels
line3.set_color('blue') # set color of line
line3.set_linestyle('-')
line3.set_marker('8') # look up under plt.plot or set_properties
line3.set_markersize(5)

line_tot.set_linewidth(3) # pixels
line_tot.set_color('orange') # set color of line
line_tot.set_linestyle('-')
line_tot.set_marker('8') # look up under plt.plot or set_properties
line_tot.set_markersize(5)

# Labeling axises, title, etc.
plt.xlabel("Months")
plt.ylabel("Total Number of Visitors")
plt.title("Chicago Public Library Visitation", color = "black")
plt.xticks(np.arange(len(headers)), headers, rotation = 45)

plt.show()


