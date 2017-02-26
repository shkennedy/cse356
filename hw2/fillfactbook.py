# Script for filling MongoDB factbook from 
# https://github.com/opendatajson/factbook.json

import os
from pymongo import MongoClient

for entry in os.listdir(os.getcwd()):
	if (os.isdir(entry)):
		os.chdir('./' + entry)
		cwd = os.getcwd()
		for factfile in os.listdir(cwd):
			MongoClient('mongoimport --db hw2 --collection factbook --file ' \
				 + cwd + '/' + factfile)
		os.chdir('..') 	
