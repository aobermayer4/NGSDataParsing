#! /bin/python3.8

from mymodule import *
import sys
#check that script use is correct
if len(sys.argv)<3:
	print ('Usage: vcf_as_search.py VCF_file outfile')
	sys.exit()
#assign arguments to file names
else:
	vcffile=sys.argv[1]
	outfile=sys.argv[2]
#generate cygwin path files
vcffile=open(cygwinpath(vcffile), 'r')
outfile=open(cygwinpath(outfile), 'w')
#user choice input
choice=int(input("Enter 1: To generate list of SNPs\nEnter 2: To generate list of insertions\nEnter 3: To generate list of deletions\nEnter 4: To generate list of positions with more that one variation\nEnter 5: to generate list with all of the above\n"))
#Choice 1: Make SNP list
if choice==1:
	snpnum=0
	linenum=0
	outfile.write('#CHROM\tPOS\tPOS\tREF\tALT\tID\tInfo\n')
	for Line in vcffile:
		Line=Line.strip('\n') #strip end of line
		if Line[0]=='#':
			continue #ignore meta and header
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		ID=Columns[2]
		Ref=Columns[3]
		Alt=Columns[4]
		Info=Columns[7]
		Info=Info.split(';')
		SAS=Info[9]
		EUR=Info[8]
		EAS=Info[5]
		AMR=Info[6]
		AFR=Info[7]
		if ',' in Alt: #if >1 alt base
			nuc=Alt.split(',')
			for i in nuc:
				Alti=i #help make one variant per line
				if len(i)==1 and len(Ref)==1: #snp
					outsnpv='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
					outfile.write(outsnpv)
					snpnum+=1
			continue
		if len(Ref)==1 and len(Alt)==1: #check for snps
			outsnp='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,AFR,AMR,EAS,EUR,SAS])+'\n'
			outfile.write(outsnp)
			snpnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	vcffile.close()
	outfile.close()
	print('Number of SNPs: ',snpnum)
#Choice 2: Make insertion list
if choice==2:
	insnum=0
	linenum=0
	outfile.write('#CHROM\tPOS\tPOS\tREF\tALT\tID\n')
	for Line in vcffile:
		Line=Line.strip('\n') #strip end of line
		if Line[0]=='#':
			continue #ignore meta and header
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		ID=Columns[2]
		Ref=Columns[3]
		Alt=Columns[4]
		Info=Columns[7]
		Info=Info.split(';')
		SAS=Info[9]
		EUR=Info[8]
		EAS=Info[5]
		AMR=Info[6]
		AFR=Info[7]
		if ',' in Alt: #if >1 alt base
			nuc=Alt.split(',')
			for i in nuc:
				Alti=i
				if len(i)>len(Ref): #insertion
					outinsv='\t'.join([Chr,Pos,Pos,Ref,Alti,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
					outfile.write(outinsv)
					insnum+=1
			continue
		if len(Ref)<len(Alt): #check for insertion
			outins='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
			outfile.write(outins)
			insnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	vcffile.close()
	outfile.close()
	print('Number of Insertions: ',insnum)
#Choice 3: Make deletion list
if choice==3:
	delnum=0
	linenum=0
	outfile.write('#CHROM\tPOS\tPOS\tREF\tALT\tID\n')
	for Line in vcffile:
		Line=Line.strip('\n') #strip end of line
		if Line[0]=='#':
			continue #ignore meta and header
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		ID=Columns[2]
		Ref=Columns[3]
		Alt=Columns[4]
		Info=Columns[7]
		Info=Info.split(';')
		SAS=Info[9]
		EUR=Info[8]
		EAS=Info[5]
		AMR=Info[6]
		AFR=Info[7]
		if ',' in Alt: #if >1 alt base
			nuc=Alt.split(',')
			for i in nuc:
				Alti=i
				if len(i)<len(Ref): #deletion
					outdelv='\t'.join([Chr,Pos,Pos,Ref,Alti,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
					outfile.write(outdelv)
					delnum+=1
			continue
		if len(Ref)<len(Alt): #check for insertion
			outdel='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
			outfile.write(outdel)
			delnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	vcffile.close()
	outfile.close()
	print('Number of Deletions: ',delnum)
#Choice 4: Make >1 variation list
if choice==4:
	varnum=0
	linenum=0
	outfile.write('#CHROM\tPOS\tPOS\tREF\tALT\tID\n')
	for Line in vcffile:
		Line=Line.strip('\n') #strip end of line
		if Line[0]=='#':
			continue #ignore meta and header
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		ID=Columns[2]
		Ref=Columns[3]
		Alt=Columns[4]
		Info=Columns[7]
		Info=Info.split(';')
		SAS=Info[9]
		EUR=Info[8]
		EAS=Info[5]
		AMR=Info[6]
		AFR=Info[7]
		if ',' in Alt: #if >1 alt base
			outvar='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
			outfile.write(outvar)
			varnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	vcffile.close()
	outfile.close()
	print('Number of positions with more than one variation: ',varnum)
#Choice 5: Make all of the above list
if choice==5:
	allnum=0
	linenum=0
	outfile.write('#CHROM\tPOS\tPOS\tREF\tALT\tID\n')
	for Line in vcffile:
		Line=Line.strip('\n') #strip end of line
		if Line[0]=='#':
			continue #ignore meta and header
		Columns=Line.split('\t')
		Chr=Columns[0]
		Pos=Columns[1]
		ID=Columns[2]
		Ref=Columns[3]
		Alt=Columns[4]
		Info=Columns[7]
		Info=Info.split(';')
		SAS=Info[9]
		EUR=Info[8]
		EAS=Info[5]
		AMR=Info[6]
		AFR=Info[7]
		if ',' in Alt: #if >1 alt base
			nuc=Alt.split(',')
			for i in nuc:
				Alti=i
				outall='\t'.join([Chr,Pos,Pos,Ref,Alti,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
				outfile.write(outall)
				allnum+=1
			continue
		outall='\t'.join([Chr,Pos,Pos,Ref,Alt,ID,EAS,AMR,AFR,EUR,SAS])+'\n'
		outfile.write(outall)
		allnum+=1
		linenum+=1
		if linenum%1000==0: #check status
			status=str(linenum)+' finished'
			sys.stderr.write(status+'\r')
	vcffile.close()
	outfile.close()
	print('Number of variations: ',allnum)
if choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5:
	print("Invalid choice\nPlease try again choosing a number 1-5")
	sys.exit()