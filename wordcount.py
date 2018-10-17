from glob import glob
import os
import re
import sys

maxLen = 30
minLen = 4
files = []
# For Testing no boundary/ argchecks
start_dir = sys.argv[1]
out_file = sys.argv[2]

pattern   = "*.*"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern))) 

wordcount = {}
out = open(out_file, "w")
i = 0
j = len(files)
for f in files:
	i = i + 1
	print str(i) + " of " + str(j)
	if not os.path.isfile(f):
		continue
	filePathClean = f[len(start_dir):]
	file=open(f)
	wordcount[filePathClean] = {}
	for word in re.findall(r"[\w']+", file.read()):
		if len(word) >= minLen and len(word) <= maxLen:
			if word not in wordcount[filePathClean]:
			    wordcount[filePathClean][word] = 1
			else:
			    wordcount[filePathClean][word] += 1
	for f,w in wordcount.items():
		for w,n in wordcount[f].items():
			out.write(f.split("/")[0]+","+"/".join(f.split("/")[1:])+","+w+","+str(n)+"\n")
	wordcount = {}
	file.close();
out.close()
