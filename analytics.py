import matplotlib.pyplot as plt
import scipy, math, random
#import tensorflow as tf
import numpy as np

def analyze():
	'''hello = tf.constant('Hello, TensorFlow!')
	sess = tf.Session()
	return sess.run(hello)'''
	pass

def anomaly_detection_meidan_filtering():
	pass

def anomaly_detection_fft():
	a = 1
	x = np.arange(1,50,0.5)
	y = np.sin(-1/x) * np.sin(x)

	y_with_outlier = np.copy(y)
	a = y
	r = np.arange(len(x)/10, len(x), len(x)/10)
	print(r)

	for i in r:
		#y_with_outlier[i] = 4 * (random.random() - 0.5 + y[i])
		a[i] = 0
		print(a)


	
