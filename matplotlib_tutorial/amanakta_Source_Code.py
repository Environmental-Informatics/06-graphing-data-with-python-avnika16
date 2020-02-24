#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to generate several plots of the requested dataset. First plot is a line 
plot of mean, max and min. Second plot is a scatter plot of Tq mean values of 
the dataset. Third plot is a barplot of the R-B index. 

Avnika Manaktala

"""

#Importing packages
import numpy as np
import matplotlib.pyplot as plt

#command to input names for the files 
fileinput= input("Enter your input file: ")
fileoutput= input("Enter your output file: ")


data= np.genfromtxt(fileinput, names=True) #Reading the data from the text file


# Creating plots
plt.figure()

#Creating top plot 
plt.subplot(311)
plt.plot(data["Year"], data["Mean"], color= "black", label= "Mean") #Plotting mean
plt.plot(data["Year"], data["Max"], color= "red", label= "Max") #Plotting max
plt.plot(data["Year"], data["Min"], color= "blue", label= "Min") #Plotting min
plt.legend(loc="upper right") # Display legend on top right 
plt.xlabel("Year") # Display x labels
plt.ylabel("Streamflow (cfs)") # Display y labels 


#Creating middle plot        
plt.subplot(312)
plt.plot(data["Year"], data["Tqmean"]*100, 'ro') #Plotting Tq mean *100
plt.xlabel("Year") # Display x labels
plt.ylabel("Tqmean (%)") # Display y labels
         
#Creating bottom plot  
plt.subplot(313)
plt.bar(data["Year"], data["RBindex"]) #Plotting R-B Index as barplot
plt.xlabel("Year") # Display x labels
plt.ylabel("R-B Index (ratio)") # Display y labels

#Adjusting space between plots to show axis clearly
plt.subplots_adjust(hspace= 0.7)

#Saving output into pdf format using user defined file name
plt.savefig(fileoutput)
