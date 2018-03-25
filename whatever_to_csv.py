import io
import pandas as pd
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("./datasets/") if isfile(join("./datasets/", f))]