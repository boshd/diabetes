import matplotlib.pyplot as plt
import os, random, math, scipy, io
from os.path import isfile, join
from os import listdir
import pre_process as pre_process
import analytics as analytics
import prepare as prepare
import metrics.metrics as metrics
import visualize as visualize
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
	files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
	prepared_data = prepare.prepare(files, 22, 57)
	visualize.visualize(prepared_data)

	# Analytics

	# Metrics

	# Random Stuff

if __name__ == '__main__':
	main()