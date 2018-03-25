import io
import pandas as pd
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("./datasets/data/") if isfile(join("./datasets/data", f)) and not f.startswith('.')]
sorted_files = sorted(onlyfiles, key=lambda item: (int(item.partition(' ')[0])
                               if item[0].isdigit() else float('inf'), item))

for filename in sorted_files:
	print("./datasets/data/"+filename)