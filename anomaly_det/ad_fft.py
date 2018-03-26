import matplotlib.pyplot as plt
import scipy, math, random, os
#import tensorflow as tf
import numpy as np

def anomaly_detection_fft(signal, threshold_freq=0.1, frequency_amplitude=.01):
	fft_of_signal = np.fft.fft(signal)
	outlier = np.max(signal) 
	if abs(np.max(signal)) > abs(np.min(signal)):
		print("nvm")
	else:
		np.min(signal)
	if np.any(np.abs(fft_of_signal[threshold_freq:]) > frequency_amplitude):
		index_of_outlier = np.where(signal == outlier)
		return index_of_outlier[0]
	else:
		return None