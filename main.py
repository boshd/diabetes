import prepare as p
import pre_process as pp
import analytics as a
import metrics as m
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings

def main():
    
	# Prepare
	x = p.prep()
	# Pre-Process

	# Analytics
	a.anomaly_detection_fft()
	# Metrics

	# Random Stuff


if __name__ == '__main__':
	main()