#! /bin/python3.8

from mymodule import *
import sys
#This script will take a file of a list of samples and run it with a VCF file of interest to pick out the columns of the particular samples you are interested in. Will show just chrom, pos, ID, ref, alt, and sample data.
if len(sys.argv)<4:
	print ('Usage: sampfind.py vcf_file sample_file output_file')
	sys.exit()
#assign arguments to file names
else:
	vcffile=sys.argv[1]
	samples=sys.argv[2]
	outfile=sys.argv[3]
#generate cygwin path files
vcffile=open(cygwinpath(vcffile), 'r')
samples=open(cygwinpath(samples), 'r')
outfile=open(cygwinpath(outfile), 'w')
SampID={} #dict to store samples
sampnum=0
for Line in samples: #add to dict
	Line=Line.strip()
	SampID[Line]=sampnum
	sampnum+=1
linenum=0
colnum=0
Nfound=0
for Line in vcffile:
	Line=Line.strip('\n')
	if Line[0]=='#': #ignore meta
		if Line[1]!='#':
			header=Line.split('\t')
			colnum=len(header) #use to get len of line
			outfile.write('\t'.join(header[0:5]))
			sample={} #dict for header
			for i in range(5,colnum):
				if(header[i] in SampID):
					outfile.write('\t'+header[i])
					sample[i]=True #for later, when true add to file
					Nfound+=1
				else:
					sample[i]=False
			outfile.write('\n')
			sys.stderr.write(str(Nfound)+' samples in the VCF file\n')
		else:
			continue
	Columns=Line.split('\t') #rest of the columns
	if Line[0]!='#':
		for i in range(5,colnum):
			if(sample[i]): #if i in header is true, add to column
				outfile.write('\t'+Columns[i])
		outfile.write('\n')
		linenum+=1
		if linenum%1000==0:
			Status=str(linenum)+' finished';
			sys.stderr.write(Status+'\r')
sys.stderr.write('Lines in vcf file:'+str(linenum))
vcffile.close() 
samples.close()
outfile.close()