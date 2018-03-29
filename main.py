import matplotlib.pyplot as plt
import os, random, math, scipy, io
from os.path import isfile, join
from os import listdir
import pre_process as pre_process
import analytics as analytics
import prepare as prepare
import metrics.confidence as conf
import visualize as visualize
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings
	    
def main():
    
	# Prepare
	files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
	sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0]) 
		if item[0].isdigit() else float('inf'), item))

	#prepared_data = prepare.prepare(files, 43, 57)
	
	array_with_all_len_metrics = conf.data_confidence(sorted_files, 60)
	print(array_with_all_len_metrics)
	
	#visualize.visualize(prepared_data)

	# Analytics

	# Metrics

	# Random Stuff

if __name__ == '__main__':
	main()