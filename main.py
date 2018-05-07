import matplotlib.pyplot as plt
import os, random, math, scipy, io
import pre_process as pre_process
import analytics as analytics
import visualize as visualize
import prepare as prepare
import patient as pt
import pandas as pd
import numpy as np

from os.path import isfile, join
from os import listdir

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings

def main():

	# Properties
	code = 62

	# Prepare patients into array
	patients = prepare.prepare_patients_()

	# Loops through patients
	for i in range(len(patients)):
		patient = patients[i]
		pre_process.pre_process(patients, patient, code)

if __name__ == '__main__':
	main()
