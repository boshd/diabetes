import matplotlib.pyplot as plt
import os, random, math, scipy
import whatever_to_csv as wtc
import pre_process as pp
import analytics as a
import prepare as p
import metrics as m
import numpy as np


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings
COLOR_PALETTE = [
		"#348ABD",
	    "#A60628",
	    "#7A68A6",
	    "#467821",
	    "#CF4457",
	    "#188487",
	    "#E24A33"]
	    
def main():
    
	# Prepare
	#x = p.prep()
	# Pre-Process

	# Analytics
	#a.anomaly_detection_fft()
	# Metrics

	# Random Stuff
	'''
	r = 1
	x = np.arange(1,50,.5)
	y = np.sin(-1/x) * np.sin(x)

	y_with_outlier = np.copy(y)

	for ii in np.arange(len(x)/10, len(x), len(x)/10.):
	    y_with_outlier[ii]= 4*(random.random()-.5) + y[ii]
	    
	outlier_positions = []
	
	for ii in range(10, y_with_outlier.size, 5):
	    outlier_position = a.anomaly_detection_fft(y_with_outlier[ii-5:ii+5])
	    if outlier_position is not None:
	        outlier_positions.append(ii + outlier_position[0] - 5)
	outlier_positions = list(set(outlier_positions))
	plt.figure(figsize=(12, 6));
	plt.scatter(range(y_with_outlier.size), y_with_outlier, c=COLOR_PALETTE[0], label='Original Signal');
	plt.scatter(outlier_positions, y_with_outlier[np.asanyarray(outlier_positions)], c=COLOR_PALETTE[-1], label='Outliers');
	plt.legend();
	plt.show()
	'''


if __name__ == '__main__':
	main()