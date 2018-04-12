import matplotlib.pyplot as plt
import os, random, math, scipy, io
from os.path import isfile, join
from os import listdir
import pre_process as pre_process
import analytics as analytics
import prepare as prepare
import metrics.confidence as conf
import visualize as visualize
import patient as pt
import numpy as np
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # disables TF GPU warnings

def main():

	# Attributes
	data = pd.DataFrame()
	patient_list = []
	confidence = 100
	id_n = 0
	code = 33

	# Prepare
	files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
	sorted_files = sorted(files, key=lambda item: (int(item.partition(' ')[0])
		if item[0].isdigit() else float('inf'), item))

	# Iterate through files and create patient for each

	for i in sorted_files[:70]:
		# increment id index
		id_n += 1

		# create dataframe df
		fullpath = "./datasets/data/" + i
		df = pd.read_csv(fullpath, # or delim_whitespace=True, #separator is whitespace
	        header=None, # no header
	        names=['DATE','TIME','CODE','VALUE']) # set columns names

		# create patient object and append into patient list
		patient = pt.Patient(id_n, df, confidence)
		patient_list.append(patient)

	# Compute confidence
	print("Patient 66:")
	conf.data_confidence(patient_list[66], code, sorted_files)
	print("Patient 23:")
	conf.data_confidence(patient_list[23], code, sorted_files)
	print("Patient 40:")
	conf.data_confidence(patient_list[40], code, sorted_files)
	print("Patient 12:")
	conf.data_confidence(patient_list[12], code, sorted_files)
	print("Patient 48:")
	conf.data_confidence(patient_list[48], code, sorted_files)

if __name__ == '__main__':
	main()
