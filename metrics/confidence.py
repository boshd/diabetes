import os, random, math, scipy
import pandas as pd
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

def data_confidence(patient, code, sorted_files):

	# Attributes
	length_arr = 0
	arr_       = []
	list_      = []

	# All patients
	for i in sorted_files[:70]:
		fullpath = "./datasets/data/" + i
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	        header=None, # no header
	        usecols=[0,1,2,3], # parse only 0,1,2,3 columns
	        names=['DATE','TIME','CODE','VALUE']) # set columns names
		df_ = df.loc[df['CODE'] == code]
		arr_.append(len(df_))
	length_arr = arr_
	avg_len = math.ceil(((np.sum(length_arr))/(len(length_arr))))

	# Our patient
	for i in patient.data:
	 	patient_df = patient.data.loc[patient.data['CODE'] == code]
	pat_len = len(patient_df)
	pat_val = patient_df[['VALUE']]

	# Confidence Model

	threshold = avg_len * 0.6
	if pat_len < threshold:
		print("Data is bad - unusable\n")	
	elif (pat_len > threshold and pat_len < avg_len):
		print("Data is ok\n")
		dummy = interp.InterpolatedUnivariateSpline(np.array(range(0, len(df1))), df1.values)
		pat_val_expanded = dummy(np.linspace(0, len(df1), avg_len))
	elif pat_len > avg_len:
		print("Data is more than good - limit?\n")


def interpolate(y, avg_len, pat_len):
	x = np.linspace(0, avg_len, num=pat_len)
	x_new = np.linspace(0, avg_len)

	new_array = interp.InterpolatedUnivariateSpline(x, y)
	print(new_array(y))
	return new_array

def return_df(df):
	return df

