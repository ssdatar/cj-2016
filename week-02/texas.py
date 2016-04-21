import csv

jobs = 0

with open('warn-act-listings-2015.csv') as c_in:
	reader = csv.reader(c_in)
	next(reader)

	for row in reader:
		if len(row[4]) is not 0:
			jobs += int(row[4])
print('In 2015,', jobs, 'people lost their jobs in Texas')
