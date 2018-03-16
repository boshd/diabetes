import matplotlib.pyplot as plt
import scipy, math, random
import tensorflow as tf
import numpy as np

def analyze():
	hello = tf.constant('Hello, TensorFlow!')
	sess = tf.Session()
	return sess.run(hello)

def anomaly_detection():
	# Signal Parameters
	number_of_samples  = 1000
	frequency_of_signal  = 5  
	sample_time = 0.001
	amplitude = 1   
	
	# Noise Parameters
	mu = 0
	sigma = 1

	signal = [amplitude * np.sin((2 * np.pi) * frequency_of_signal * ii * sample_time) for ii in range(number_of_samples)]
	s_time = [ii * sample_time for ii in range(number_of_samples)]
	noise = [random.gauss(mu, sigma) for _ in range(number_of_samples)]
	signal_with_noise = [ii + jj for ii, jj in zip(signal, noise)]

	fft_of_signal_with_noise = np.fft.fft(signal_with_noise)
	f = np.fft.fftfreq(len(fft_of_signal_with_noise),sample_time)

	def bandpass_filter(x, freq, frequency_of_signal=frequency_of_signal, band = 0.05):
	    if (frequency_of_signal - band) < abs(freq) < (frequency_of_signal + band):
	        return x
	    else:
	        return 0

	F_filtered = np.asanyarray([bandpass_filter(x,freq) for x,freq in zip(fft_of_signal_with_noise, f)]);
	filtered_signal = np.fft.ifft(F_filtered);

	plt.plot(filtered_signal)
	plt.title('Filtered Signal u/ bandpass filter')
	plt.show()
	
