from glob import glob
import os
import re
import sys
import logging
import pprint
from sets import Set

log = logging.getLogger('AnalysePage')
logging.basicConfig(filename='out.log',level=logging.DEBUG)

# For Testing no boundary/ argchecks
start_dir = sys.argv[1]
seite = sys.argv[2]

pattern   = "*.*"

class FileWalker:
	def __init__(self, startPath):
		log.debug("__init__ exec")
		self.__files = []
		self.__startPath = startPath
	def walk(self):
		log.debug("walk exec, start dir: " + self.__startPath)
		self.__files = []	
		for dir,_,_ in os.walk(self.__startPath):
			self.__files.extend(glob(os.path.join(dir,pattern)))
		log.info("walk done, found files: " + str(len(self.__files)))
	def getFileList(self):
		if len(self.__files) == 0:
			self.walk()
		return self.__files
	def getStartPathLen(self):
		return len(self.__startPath)

class Analyzer:
	def __init__(self, fileWalker):
		log.debug("__init__ exec")
		self.__fileWalker = fileWalker
		self.__result = {}
		self.__result["files"] = {}
		self.__result["global"] = {}
		self.__result["global"]["pdfDocs"] = Set()
		self.__result["global"]["antraege"] = Set()
	def analyze(self):
		sumFiles = len(self.__fileWalker.getFileList())
		actFile = 0
		for f in self.__fileWalker.getFileList():
			actFile = actFile + 1
			log.debug("analyze " + str(actFile) + " of " + str(sumFiles))
			if not os.path.isfile(f):
				continue
			file = open(f)
			text = file.read()
			file.close();
			self.__result["files"][actFile] = {}
			self.__result["files"][actFile]["path"] = f[self.__fileWalker.getStartPathLen():]
			# Analyseschritte
			self.__result["global"]["pdfDocs"] = self.__result["global"]["pdfDocs"].union(self.findPdf(text))
			self.__result["global"]["antraege"] = self.__result["global"]["antraege"].union(self.findAntraege(text))
	def findPdf(self, text):
			files = re.findall(r'href="(.*pdf)"', text)
			return set(files)
	def findAntraege(self, text):
			words = re.findall(r'\b(\w*antrag)\b', text)
			return set(words)
	def printResult(self):
		pprint.pprint(self.__result)
			
fw = FileWalker(start_dir + "/" + seite)
an = Analyzer(fw)
an.analyze()
an.printResult()

