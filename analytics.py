import matplotlib.pyplot as plt
import scipy, math, random, os
from PyNomaly import loop
#import tensorflow as tf
import numpy as np

# Analytics MAIN engine

def analyze(patient, code):

	for i in patient.data:
	 	patient_df = patient.data.loc[patient.data['CODE'] == code]
	pat_val_arr = patient_df[['VALUE']]

	m = loop.LocalOutlierProbability(pat_val_arr).fit()
	scores = m.local_outlier_probabilities
	print(scores)
		
	#else: 
		# dont begin analysis and request more data


	
