#! /bin/python3.9.5

import sys
import os

#input: script manifest_in.txt /path/to/files/ manifest_out.txt

manin = open(sys.argv[1], 'r')
bampath = sys.argv[2]
manout = open(sys.argv[3], 'w')

## scan directory for .bam folders and add to list
# blank list to hold folder names
bamfiles=[]
# for every file in bam directory, add and append to list
for folder in os.listdir(bampath):
	if os.path.isdir(os.path.join(bampath,folder)) == True:
		bamfiles.append(folder)

# check if bam in manifest is already in bam folder
# add to new manifest file if not
for line in manin:
	line = line.strip('\n')
	col = line.split('\t')
	folID = col[0]
	folData = '\t'.join(col[1:])
	if folID not in bamfiles:
		manout.write(folID+'\t'+folData+'\n')
	else:
		continue

manin.close()
manout.close()