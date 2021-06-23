#! /bin/python3.7.2
import sys
import os
import pysam
import numpy as np

## how to use script
if len(sys.argv)<5:
	print('Usage: basescovered.py /path/to/bam/files/ ref.fai bamfilelist.txt sampledepths5.txt sampledepths10.txt')
	sys.exit()
else:
	bampath=sys.argv[1]
	reffile=sys.argv[2]
	bamfilelist=sys.argv[3]
	depthfile5=sys.argv[4]
	depthfile10=sys.argv[5]

## open files
reffile=open(reffile, 'r')
bamfilelist=open(bamfilelist, 'w')
depthfile5=open(depthfile5, 'w')
depthfile10=open(depthfile10, 'w')

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
covlistall=[] #contains all read depths 1>=
dp5array=np.array(['Sample','DepthFraction','MeanDepth','MedianDepth']) #blank np array
dp10array=np.array(['Sample','DepthFraction','MeanDepth','MedianDepth']) #blank np array
# for loop to go through .bam files
for file in bamfiles:
	covlist=[] #temp depth list
	posgt10temp=0
	posgt5temp=0
	bamf=pysam.AlignmentFile(file, 'rb') #opens .bam for reading
	for pilecol in bamf.pileup('chrM', FastaFile=reffile): #pileup function
		covlist.append(pilecol.n) #extracts coverage to temp list
		covlistall.append(pilecol.n) #extracts coverage to full list
	for i in covlist: #check for positions by read depth
		postot+=1
		if postot%10==0: #status message while reading files
				status=str(postot)+' bases checked'
				sys.stderr.write(status+'\r')
		if i >= 10:
			posgt10+=1
			posgt10temp+=1
			posgt5+=1
			posgt5temp+=1
		elif i >= 5:
			posgt5+=1
			posgt5temp+=1
	depfr5=(round((posgt5temp/16569),4)) #depth fraction >5
	depfr10=(round((posgt10temp/16569),4)) #depth fraction >10
	meandep=(round((sum(covlist)/16569), 2)) #mean depth
	meddep=(np.median(covlist)) #median depth
	#add to depth array
	dp5array=np.vstack((dp5array,[file,depfr5,meandep,meddep]))
	dp10array=np.vstack((dp10array,[file,depfr10,meandep,meddep]))
	bamf.close() #close bam file

## save numpy array to outfile
np.savetxt(depthfile5, dp5array, fmt='%s', delimiter='\t')
np.savetxt(depthfile10, dp10array, fmt='%s', delimiter='\t')

## find fraction of read depths >5 and >10
dpfr5t=round((posgt5/posmt), 4)
dpfr10t=round((posgt10/posmt), 4)

## close files
reffile.close()
bamfilelist.close()
depthfile5.close()
depthfile10.close()

## write outcome in console
# number of bases out of bases total
print(str(posgt10)+' bases with read depth greater than 10 out of '+str(posmt)+' bases read')
print(str(posgt5)+' bases with read depth greater than 5 out of '+str(posmt)+' bases read')
# fraction of bases total
print(str(dpfr5t)+' = Fraction of bases covered with a read depth greater than 5 out of '+str(posmt)+' bases read')
print(str(dpfr10t)+' = Fraction of bases covered with a read depth greater than 10 out of '+str(posmt)+' bases read')
# mean/median depth
print(str(round((sum(covlistall)/posmt), 2))+' average read depth')
print(str(np.median(covlistall))+' meadian read depth not counting zeros')