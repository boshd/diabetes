import matplotlib.pyplot as plt
import os, random, math, scipy, io
import pandas as pd
import numpy as np
'''
df = pd.read_csv("./data-01", #or delim_whitespace=True, #separator is whitespace
                 header=None, #no header
                 usecols=[0,1,2,3], #parse only 3,4,6 columns
                 names=['a','b','c','d']) #set columns names
'''
'''
with open('./data-01') as data:
	plaintext = data.read()
	data.write(plaintext.replace(',', ' '))
'''

f_read = open('./data-01')
file_contents = f_read.read()
f_write = open('./data-01', 'w')
f_write.write(file_contents.replace('	', ', '))
f_write.close()
f_read = open('./data-01')
file_contents = f_read.read()
f_write = open('./data-01', 'w')
f_write.write(file_contents.replace('"', ''))
f_write.close()
'''
filename = './data-01.txt'
column_names = ['x','y','z','w']
df = pd.read_csv(filename, sep='\s+',header=None)

print(df)
'''

'''
data = pd.read_csv("datae.csv")
### Data extraction from csv file ###
data.columns = ["Time", "temperature", "icon", "humidity", "visibility", "summary", "apparentTemperature", "pressure", "windSpeed", "epochTime", "windBearing", "precipIntensity", "dewPoint", "precipProbability", "Apartment1",  "Apartment2",  "Apartment3",  "Apartment4",  "Apartment5"]
time = list(data.Time)
temp = list(data.temperature)
humi = list(data.humidity)
visi = list(data.visibility)
atmp = list(data.apparentTemperature)
pres = list(data.pressure)
wspd = list(data.windSpeed)
etim = list(data.epochTime)
wbrg = list(data.windBearing)
prei = list(data.precipIntensity)
dpnt = list(data.dewPoint)
prep = list(data.precipProbability)
apt1 = list(data.Apartment1)
apt2 = list(data.Apartment2)
apt3 = list(data.Apartment3)
apt4 = list(data.Apartment4)
apt5 = list(data.Apartment5)

def prep():
	# do stuff w/ data
	pass
'''