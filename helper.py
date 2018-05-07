import matplotlib.pyplot as plt
import os, random, math, scipy
import scipy.interpolate as interp
import pandas as pd
import numpy as np
import metrics.helper_metrics as hm

def validate_data(patients, code):
	pass
	'''
	if code == 33:
		if hm.whatsTheAverage(patients, code):
			
		return True
	elif code == 58:
		return True
	elif code == 59: 
		return True
	elif code == 60: 
		return True
	elif code == 61: 
		return True
	elif code == 62: 
		return True
	elif code == 63: 
		return True
	elif code == 66: 
		return True
	elif code == 68: 
		return True
	else:
		print("invalid code.")
		return False
	'''

def interpolate(val_arr, length):
	dummy = interp.InterpolatedUnivariateSpline(np.array(range(0, len(val_arr))), val_arr.values)
	val_arr_expanded = dummy(np.linspace(0, len(val_arr), length))
	return val_arr_expanded