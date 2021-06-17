#! /bin/python3.8

from mymodule import *
import sys
#This script will take the SNP file from the vcf_ChoiceSearch script and add if there was a transition or transversion
#check that script use is correct
if len(sys.argv)<2:
	print ('Usage: snptr_cluster.py SNP_file outfile')
	sys.exit()
#assign arguments to file names
else:
	snpfile=sys.argv[1]
	outfile=sys.argv[2]
#generate cygwin path files
snpfile=open(cygwinpath(snpfile), 'r')
outfile=open(cygwinpath(outfile), 'w')
#user choice input
choice=int(input("Enter 1: To generate list of SNP transitions\nEnter 2: To generate list of SNP transversions\nEnter 3: To generate list of both\n"))
#Choice 1: list of transitions
if choice==1:
	trsnum=0
	linenum=0
	for Line in snpfile:
		Line=Line.strip('\n')
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		Ref=Columns[3]
		Alt=Columns[4]
		ID=Columns[5]
		if Ref=='A' and Alt=='G':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='G' and Alt=='A':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='C' and Alt=='T':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='T' and Alt=='C':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	snpfile.close()
	outfile.close()
	print('Number of Transitions in SNP file: ',trsnum)
#Choice 2: list of transversions
if choice==2:
	trvnum=0
	linenum=0
	for Line in snpfile:
		Line=Line.strip('\n')
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		Ref=Columns[3]
		Alt=Columns[4]
		ID=Columns[5]
		if Ref=='A' and Alt=='T':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='T' and Alt=='A':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='A' and Alt=='C':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='C' and Alt=='A':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='G' and Alt=='C':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='C' and Alt=='G':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='G' and Alt=='T':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='T' and Alt=='G':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	snpfile.close()
	outfile.close()
	print('Number of Transversions in SNP file: ',trvnum)
#Choice 3: list all
if choice==3:
	trsnum=0
	trvnum=0
	linenum=0
	for Line in snpfile:
		Line=Line.strip('\n')
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		Ref=Columns[3]
		Alt=Columns[4]
		ID=Columns[5]
		if Ref=='A' and Alt=='G':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transition'])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='G' and Alt=='A':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transition'])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='C' and Alt=='T':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transition'])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		elif Ref=='T' and Alt=='C':
			trs='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transition'])+'\n'
			outfile.write(trs+'\n')
			trsnum+=1
		if Ref=='A' and Alt=='T':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='T' and Alt=='A':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='A' and Alt=='C':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='C' and Alt=='A':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='G' and Alt=='C':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='C' and Alt=='G':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='G' and Alt=='T':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		elif Ref=='T' and Alt=='G':
			trv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,'Transversion'])+'\n'
			outfile.write(trv+'\n')
			trvnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	snpfile.close()
	outfile.close()
	ptrs=(trsnum/linenum)*100
	ptrv=(trvnum/linenum)*100
	print('Number of Transitions in SNP file: ',trsnum,'::',round(ptrs,2),'% Transitions''\n''Number of Transversions in SNP file: ',trvnum,'::',round(ptrv,2),'% Transversions')
if choice!=1 and choice!=2 and choice!=3:
	print("Invalid choice\nPlease try again choosing a number 1-3")
	sys.exit()