import os
from Bio import *

folderPath = "datum/FASTAs/"

for filename in os.listdir(folderPath):
    for filename2 in os.listdir(folderPath):
        if filename != filename2:
            fullFileName = folderPath + filename
            fullFileName2 = folderPath + filename2
            