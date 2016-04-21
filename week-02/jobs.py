import glob
import csv

all_csvs = glob.glob('CAWARN-*.csv')

jobs_lost = 0

for index, f in enumerate(all_csvs):
    with open(f, 'r') as c_in:
        print('Reading file:', f)
        reader = csv.reader(c_in)
        next(reader)

        if index <= 2:
            for row in reader:
                jobs_lost += int(row[2])

        else:
            for row in reader:
                jobs_lost += int(row[5])

print('Total jobs lost:', jobs_lost)