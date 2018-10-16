from glob import glob
import os
import re

maxLen = 30
minLen = 4
files = []
start_dir = "/home/developer/staedte/data/"
pattern   = "*.aspx"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern))) 

wordcount = {}
for f in files:
	file=open(f)
	wordcount[f] = {}
	for word in re.findall(r"[\w']+", file.read()):
		if len(word) >= minLen and len(word) <= maxLen:
			if word not in wordcount[f]:
			    wordcount[f][word] = 1
			else:
			    wordcount[f][word] += 1

	file.close();
for f,w in wordcount.items():
	for w,n in wordcount[f].items():
		print f,w,n

