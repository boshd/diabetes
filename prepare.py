import os, random, math, scipy, io
from os.path import isfile, join
import matplotlib.pyplot as plt
from os import listdir
import pandas as pd
import numpy as np

# Attributes
dataframe = pd.DataFrame()
list_ = []
index = 0

files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0])
                               if item[0].isdigit() else float('inf'), item))

for filename in sorted_files:
	fullpath = "./datasets/data/" + filename
	f_read = open(fullpath)
	file_contents = f_read.read()
	f_write = open(fullpath, 'w')
	f_write.write(file_contents.replace('	', ', '))
	f_write.close()
	f_read = open(fullpath)
	file_contents = f_read.read()
	f_write = open(fullpath, 'w')
	f_write.write(file_contents.replace('"', ''))
	f_write.close()
	index += 1
	print("reached file ", index)

for filename in sorted_files:
	fullpath = "./datasets/data/" + filename
	df = pd.read_csv(fullpath, #or delim_whitespace=True, #separator is whitespace
                 header=None, #no header
                 usecols=[0,1,2,3], #parse only 3,4,6 columns
                 names=['DATE','TIME','CODE','VALUE']) #set columns names
	list_.append(df)

dataframe = pd.concat(list_)
print(dataframe)


def prep():
	# do stuff w/ data
	pass
