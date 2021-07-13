#! /bin/python3.9.5

import sys
import os
import pandas as pd

if len(sys.argv) < 3 :
	print('Usage: RenamerByMap.py /path/to/Sample/Folders/ SampleSheet.tsv')
	sys.exit()
else :
	filepath=sys.argv[1]
	namemap=open(sys.argv[2], 'r')

## make pandas df with namemap
namemap=pd.read_csv(namemap, sep='\t', index_col=0)
#spaces in header were manually taken out. Will be looking into coding that piece in.


## will rename from deepest file out to folders in directory
#  rename is based off of 'CaseID' and first character of 'SampleType' found in 'namemap' + extensions
#  some 'CaseID's have 2 sample of the same type and are seperated by a comma and space.
#  will look into aking the white space out.

for folder in os.listdir(filepath) : #loop through given path for sub-directories
	for file in os.listdir(os.path.join(filepath, folder)) : #loop through folders for files/sub-dir
		if os.path.isdir(os.path.join(filepath, folder, file)) == True : #if sub-dir exists
			for file2 in os.listdir(os.path.join(filepath,folder, file)) : #loop through sub-dir for files
				ext=file2.split('.')[1:] #extraxt file extensions
				ext='.'.join(ext) #join extensions
				newID=namemap.at[folder,'CaseID']
				if ',' in newID :
					newID=newID.split(',')[0]
				src=os.path.join(filepath, folder, file, file2) #old path to file
				dst=os.path.join(filepath, folder, file, #new path to file
					newID+'_'+namemap.at[folder,'SampleType'][0]+'.'+str(ext))
				os.rename(src,dst) #rename function
		else :
			ext=file.split('.')[1:]
			ext='.'.join(ext)
			newID=namemap.at[folder,'CaseID']
			if ',' in newID :
				newID=newID.split(',')[0]
			src=os.path.join(filepath, folder, file)
			dst=os.path.join(filepath, folder,
				newID+'_'+namemap.at[folder,'SampleType'][0]+'.'+str(ext))
			os.rename(src,dst)
	newID=namemap.at[folder,'CaseID']
	if ',' in newID :
		newID=newID.split(',')[0]
	src=os.path.join(filepath, folder)
	dst=os.path.join(filepath, newID+'_'+namemap.at[folder,'SampleType'][0])
	foldernew=os.rename(src, dst)
