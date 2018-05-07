import analytics as analytics
import metrics.confidence as conf

def pre_process(patients, patient, code):
	if conf.data_confidence(patients, patient, code):
		analytics.analyze(patient, code)
	#else:
	#	print("bad data, can't be analyzed\n")
		

def pre_process_data():
	pass