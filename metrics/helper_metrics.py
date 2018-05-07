import os, random, math, scipy
import pandas as pd
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

def whatsTheAverage(patients, code):

	# Attributes
	arr_ = []

	# All patients
	for i in patients[:70]:
		df_ = i.data.loc[i.data['CODE'] == code]
		arr_.append(len(df_))
	length_arr = arr_
	avg = math.ceil(((np.sum(length_arr))/(len(length_arr))))

	return avg