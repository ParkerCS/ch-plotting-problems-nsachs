#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.

import csv
import matplotlib as plt
import numpy as py

file = open("chi_life_expectancy.txt", "r")

# Reading the file into a list
life_expectancy = []
reader = csv.reader(file, delimiter = '\t')
for line in reader:
    life_expectancy.append(line)
#print(life_expectancy)

#Scanning the list to get the life expectancy in 2010
life_expectancy_2010 = []
for i in range(1,len(life_expectancy)):
    life_expectancy_2010.append(float(life_expectancy[i][8]))
print(life_expectancy_2010)

#Scanning for only the community names and creating a list
community_list = []
for i in range(1,len(life_expectancy)):
    community_list.append(life_expectancy[i][1])
community_list = life_expectancy[1:][1]
print(community_list)

#x = community name
#y = life expectancy in 2010
'''
plt.figure(tight_layout = True, figsize = [12,5])

plt.bar(np.arange(len(life_1990_list)), life_2000_list, life_2010_list))
plt.ylim([50, 80])
plt.text(35, 61.8, "Minimum = ")
plt.arrow(35, 61.8, 5, 5, head_width = 1, color = "black")
'''
