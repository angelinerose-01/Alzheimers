import requests

url = 'http://localhost:5000/results'
# r = requests.post(url,json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400})

r = requests.post(url,jason={
	'Subject ID' :'OAS2_0001',
	'Visit' : 1 ,
	'MR Delay' : 0 ,
	'M/F' : M, 
	'Hand' : R, 
	'Age' : 87 ,
	'EDUC' : 14,
	'SES' : 2,
	'MMSE' :27 ,
	'CDR' : 0,
	'eTIV' :1987 ,
	'nWBV' : 0.69,
	'ASF' : 0.883})




print(r.json())