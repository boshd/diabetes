import os, io
from os.path import isfile, join
from os import listdir

def fix_data(sorted_files, index):
	for filename in sorted_files:
		fullpath = "./datasets/data/" + filename
		f_read = open(fullpath)
		file_contents = f_read.read()
		f_write = open(fullpath, 'w')
		f_write.write(file_contents.replace('	', ', '))
		f_write.close()
		f_read = open(fullpath)
		file_contents = f_read.read()
		f_write = open(fullpath, 'w')
		f_write.write(file_contents.replace('"', ''))
		f_write.close()
		f_read = open(fullpath)
		file_contents = f_read.read()
		f_write = open(fullpath, 'w')
		f_write.write(file_contents.replace('0Hi', '0'))
		f_write.close()
		index += 1
		print("reached file ", index)

	return index;
