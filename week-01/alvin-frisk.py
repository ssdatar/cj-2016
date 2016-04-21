import csv
from csv import DictReader

with open('2011.csv', 'r', encoding='utf-8', errors='ignore') as infile:
	datarows = list(DictReader(infile))

stopped = []
teens = []
harlem = []

for row in datarows:
	row['pct'] = int(row['pct'])
	row['age'] = int(row['age'])

	if row['datestop'] == '6032011':
		stopped.append(row)

for s in stopped:
	if s['age'] in range(16,19) and s['pct'] == 28:
		teens.append(s)

#Seems like him. The street intersection is nearly the same as mentioned in the video
alvin = teens[1]

print(alvin)
print('Seems like him. The street intersection',
      'is nearly the same as mentioned in the video')