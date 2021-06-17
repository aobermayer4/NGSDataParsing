#! /bin/python3.7.2
import sys
import os
import pysam
import numpy as np

## how to use script
if len(sys.argv)<4:
	print('Usage: basescovered.py /path/to/bam/files/ ref.fa bamfilelist.txt')
	sys.exit()
else:
	bampath=sys.argv[1]
	reffile=sys.argv[2]
	bamfilelist=sys.argv[3]

## open files
reffile=open(reffile, 'r')
bamfilelist=open(bamfilelist, 'w')

## scan directory for .bam files and add filenames to list
# blank list to hold names
bamfiles=[]
bamnum=0
# for every file in bam directory, add and append to list
for file in os.listdir(bampath):
	if os.path.isfile(os.path.join(bampath, file)): #reads files in bampath
		if file.endswith('.bam'):                   #checks for .bam ending
			bamfiles.append(file)                   #adds file to list
			bamfilelist.write(file+'\n')            #write file to outfile
			bamnum+=1

## Count total MT positions out of all samples
posmt=(16569*bamnum)

## perform mpileup and extract depth count
# set counters
posgt10=0
posgt5=0
postot=0
covlistall=[]
# for loop to go through .bam files
for file in bamfiles:
	covlist=[]
	bamf=pysam.AlignmentFile(file, 'rb')                    #opens .bam for reading
	for pilecol in bamf.pileup('MT', FastaFile=reffile):    #pileup function
		covlist.append(pilecol.n)                           #extracts coverage to temp list
		covlistall.append(pilecol.n)                        #extracts coverage to full list
	for i in covlist:                                       #check for positions by read depth
		postot+=1
		if postot%100==0:                                   #status message while reading files
				status=str(postot)+' bases checked'
				sys.stderr.write(status+'\r')
		if i >= 10:
			posgt10+=1
			posgt5+=1
		elif i >= 5:
			posgt5+=1
	bamf.close() #close bam file

## find fraction of read depths >5 and >10
# this is out of positions with depth 1>
dpfr5=round((posgt5/postot), 4)
dpfr10=round((posgt10/postot), 4)
# this is with all positions sequenced
dpfr5t=round((posgt5/(16569*bamnum)), 4)
dpfr10t=round((posgt10/(16569*bamnum)), 4)

## close files
reffile.close()
bamfilelist.close()

## write outcome in console
# number of bases out of bases read
print(str(posgt10)+' bases with read depth greater than 10 out of '+str(postot)+' bases read')
print(str(posgt5)+' bases with read depth greater than 5 out of '+str(postot)+' bases read')
# number of bases out of bases total
print(str(posgt10)+' bases with read depth greater than 10 out of '+str(posmt)+' bases read')
print(str(posgt5)+' bases with read depth greater than 5 out of '+str(posmt)+' bases read')
# fraction of bases read
print(str(dpfr5)+' = Fraction of bases covered with a read depth greater than 5 out of '+str(postot)+' bases read')
print(str(dpfr10)+' = Fraction of bases covered with a read depth greater than 10 out of '+str(postot)+' bases read')
# fraction of bases total
print(str(dpfr5t)+' = Fraction of bases covered with a read depth greater than 5 out of '+str(posmt)+' bases read')
print(str(dpfr10t)+' = Fraction of bases covered with a read depth greater than 10 out of '+str(posmt)+' bases read')
# mean/median depth
print(str(round((sum(covlistall)/postot), 2))+' average read depth not counting zeros')
print(str(round((sum(covlistall)/posmt), 2))+' average read depth counting zeros')
print(str(np.median(covlistall))+' meadian read depth not counting zeros')