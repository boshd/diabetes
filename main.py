import prepare as p
import pre_process as pp
import analytics as a
import metrics as m
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings

def main():
    
	# Prepare
	x = p.prep()
	print(x)
	# Pre-Process

	# Analytics
	y = a.analyze()
	a.anomaly_detection()
	# Metrics

	# Random Stuff


if __name__ == '__main__':
	main()