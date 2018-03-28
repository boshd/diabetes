import os, random, math, scipy, io
from os.path import isfile, join
import matplotlib.pyplot as plt
from os import listdir
import fix_data as fix
import pandas as pd
import numpy as np

# Attributes
dataframe = pd.DataFrame()
gluco_df = pd.DataFrame()
list_ = []
gluco_list = []
index = 0
i = 0

files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0])
                               if item[0].isdigit() else float('inf'), item))

fix.fix_data(sorted_files, index)

for filename in sorted_files[:0]:
	fullpath = "./datasets/data/" + filename
	df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
                header=None, # no header
                usecols=[0,1,2,3], # parse only 0,1,2,3 columns
                names=['DATE','TIME','CODE','VALUE']) # set columns names
	i += 1
	if i>1:
		list_.append(df)
	

if i>1:
	dataframe = pd.concat(list_)
else:
	dataframe = df

#print(dataframe)

gluco_df = dataframe.loc[dataframe['CODE'] == 60]

for i in gluco_df.VALUE:
	gluco_list.append(i)

print(gluco_df)
print(gluco_list)


def prep():
	# do stuff w/ data
	pass
