import matplotlib.pyplot as plt
import os, random, math, scipy, io
from os.path import isfile, join
from os import listdir
import pre_process as pre_process
import analytics as analytics
import visualize as visualize
import patient as pt
import numpy as np
import pandas as pd

def prepare_patients():

	# Attributes
	data = pd.DataFrame()
	patient_list = []
	confidence = 100
	id_n = 0
	code = 33

	# Prepare
	files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
	sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0])
		if item[0].isdigit() else float('inf'), item))

	# Iterate through files and create patient for each given file
	# This will be altered upon integration of a real-time OR quasi-real-time system
	for i in sorted_files[:70]:
		# increment id index
		id_n += 1
		# create dataframe df
		fullpath = "./datasets/data/" + i
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	        header=None, # no header
	        names=['DATE','TIME','CODE','VALUE']) # set columns names
		# create patient object and append into patient list
		patient = pt.Patient(id_n, df, confidence)
		patient_list.append(patient)

	# Compute confidence
	#print("Patient 66:")
	#pre_process.process(patient_list[66], code, sorted_files)

	return patient_list

def prepared(sorted_files, file_index, code):
	# Attributes
	dataframe = pd.DataFrame()
	gluco_df = pd.DataFrame()
	list_ = []
	gluco_list = []
	index = 0
	i = 0

	fix.fix_data(sorted_files, index)
	for filename in sorted_files[:file_index]:
		fullpath = "./datasets/data/" + filename
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	                header=None, # no header
	                usecols=[0,1,2,3], # parse only 0,1,2,3 columns
	                names=['DATE','TIME','CODE','VALUE']) # set columns names
		i += 1
	
	dataframe = df

	return dataframe
	
def prepare_all(files):
	# Attributes
	dataframe = pd.DataFrame()
	code_df = pd.DataFrame()
	list_ = []
	index = 0
	i = 0

	sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0]) 
		if item[0].isdigit() else float('inf'), item))

	fix.fix_data(sorted_files, index)

	for filename in sorted_files[:70]:
		fullpath = "./datasets/data/" + filename
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	                header=None, # no header
	                usecols=[0,1,2,3], # parse only 0,1,2,3 columns
	                names=['DATE','TIME','CODE','VALUE']) # set columns names
		list_.append(df)

	dataframe = pd.concat(list_)

	return dataframe	
