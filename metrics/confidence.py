import os, random, math, scipy
import pandas as pd
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

def data_confidence(patients, patient, code):

	# Attributes
	length_arr = 0
	arr_       = []
	list_      = []
	isAnalyzable = False

	# All patients
	for i in patients[:70]:
		df_ = i.data.loc[i.data['CODE'] == code]
		arr_.append(len(df_))
	length_arr = arr_
	avg_len = math.ceil(((np.sum(length_arr))/(len(length_arr))))

	# Our patient
	for i in patient.data:
	 	patient_df = patient.data.loc[patient.data['CODE'] == code]
	pat_len = len(patient_df)
	pat_val_arr = patient_df[['VALUE']]

	# Confidence Model (comparing all patients to THE patient)
	threshold = avg_len * 0.6
	if pat_len < threshold:
		pass
	elif (pat_len > threshold and pat_len < avg_len):
		dummy = interp.InterpolatedUnivariateSpline(np.array(range(0, len(pat_val_arr))), pat_val_arr.values)
		pat_val_arr_expanded = dummy(np.linspace(0, len(pat_val_arr), avg_len))
		isAnalyzable = True
	elif pat_len > avg_len:
		isAnalyzable = True
	return isAnalyzable


def interpolate(y, avg_len, pat_len):
	x = np.linspace(0, avg_len, num=pat_len)
	x_new = np.linspace(0, avg_len)

	new_array = interp.InterpolatedUnivariateSpline(x, y)
	print(new_array(y))
	return new_array

def return_df(df):
	return df

