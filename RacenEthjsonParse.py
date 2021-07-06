#! /bin/python3.9.5

import sys
import json

data = json.load(open(sys.argv[1], 'r'))

for i in data:
	caseID = i['exposures'][0]['submitter_id']
	caseID = caseID[:-4]
	race = i['demographic']['race']
	ethnicity = i['demographic']['ethnicity']
	status = i['demographic']['vital_status']
	print('caseID:',caseID,'\n\trace:',race,'\n\tethnicity:',ethnicity,'\n\tvital_status:',status)
