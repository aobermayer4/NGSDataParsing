#! /bin/python3.8

from mymodule import *
import sys
#This script takes a given list of SNPs and searches it along with a VCF file and parses out the particular SNPs you are interested in while keeping all sample data.
if len(sys.argv)<4:
	print ('Usage: vcf_snpfinder.py VCF_file snp_file output_file')
	sys.exit()
#assign arguments to file names
else:
	vcffile=sys.argv[1]
	snpfile=sys.argv[2]
	outfile=sys.argv[3]
#generate cygwin path files
vcffile=open(cygwinpath(vcffile), 'r')
snpfile=open(cygwinpath(snpfile), 'r')
outfile=open(cygwinpath(outfile), 'w')
#make snp list
snpID=[]
for Line in snpfile:
	Line=Line.strip()
	snpID.append(Line)
linenum=0
for Line in vcffile:
	Line=Line.strip('\n')
	if Line[0]=='#':
		if Line[1]!='#': #keep header
			outfile.write('\t'+Line+'\n')
		else:
			continue
	Columns=Line.split('\t')
	ID=Columns[2]
	for i in snpID:
		if i==ID:
			outfile.write('\t'+Line+'\n')
	linenum+=1
	if linenum%1000==0:
		status=str(linenum)+' finished'
		sys.stderr.write(status+'\r')
vcffile.close()
snpfile.close()
outfile.close()