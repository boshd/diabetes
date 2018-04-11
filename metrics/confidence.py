import os, random, math, scipy
import pandas as pd
import numpy as np

def data_confidence(patient, code, sorted_files):

	# Attributes
	length_arr = 0
	arr_       = []
	list_      = []

	for i in sorted_files[:70]:
		fullpath = "./datasets/data/" + i
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	        header=None, # no header
	        usecols=[0,1,2,3], # parse only 0,1,2,3 columns
	        names=['DATE','TIME','CODE','VALUE']) # set columns names
		df_ = df.loc[df['CODE'] == code]
		arr_.append(len(df_))
	length_arr = arr_
	avg = ((np.sum(length_arr))/(len(length_arr)))

	# patient
	for i in patient.data:
	 	patient_df = patient.data.loc[patient.data['CODE'] == code] 

	#print(patient_df)

	'''

	if len(df_) < 20:
		print("not admissable -- this will affect the confidence metric ")

	for i in length_arr:
		index += 1
		if i <= 10:
			return np.around(average)
			#supposed to return confidence but we're still figuring that out ayy
	'''

def conf(length):
	pass

def interpolate():
	pass
