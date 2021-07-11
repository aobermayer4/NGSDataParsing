#! /bin/python3.9.5

import sys
import json
import numpy as np


data = json.load(open(sys.argv[1], 'r'))
clinout = open('ClinicalStats.tsv', 'w')

clinical=np.array(['CaseID','Race','Ethnicity','Vital_Status','Smoker_Status']) #blank np array


for i in data:
	caseID = i['exposures'][0]['submitter_id']
	caseID = caseID[:-4]
	race = i['demographic']['race']
	ethnicity = i['demographic']['ethnicity']
	vitals = i['demographic']['vital_status']
	smoker = i['exposures'][0]['tobacco_smoking_status']
	clinical=np.vstack((clinical,[caseID,race,ethnicity,vitals,smoker]))

np.savetxt(clinout, clinical, fmt='%s', delimiter='\t')

clinout.close()












#	print('caseID:',caseID,
#		'\n\trace:',race,
#		'\n\tethnicity:',ethnicity,
#		'\n\tvital_status:',vitals,
#		'\n\tTobacco_Smoking_Status:',smoker)
