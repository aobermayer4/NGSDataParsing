#! /bin/python3.9.5

import sys
import os
import pandas as pd

if len(sys.argv) < 3 :
	print('Usage: NameMapperTest.py /path/to/Sample/Folders/ SampleSheet.tsv')
	sys.exit()
else :
	filepath=sys.argv[1]
	namemap=open(sys.argv[2], 'r')

## make pandas df with namemap
namemap=pd.read_csv(namemap, sep='\t', index_col=0)


for folder in os.listdir(filepath) :
	src=os.path.join(filepath, folder)
	dst=os.path.join(filepath, namemap.at[folder,'SampleID']+'_'+namemap.at[folder,'SampleType'][0])
	foldernew=os.rename(src, dst)
	print(foldernew)


#### IN PROGRESS ####
# will be adding script to rename files within folders
# just troubleshooting (: