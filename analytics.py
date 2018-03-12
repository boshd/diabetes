import scipy, math, random
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def analyze():
	hello = tf.constant('Hello, TensorFlow!!!')
	sess = tf.Session()
	return sess.run(hello)

def anomaly_detection():
	print("Anomaly Detection Module")
	
