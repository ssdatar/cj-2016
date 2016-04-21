import csv
import os
import re

indiv_affected = 0
the_file = os.path.join('breach_report.csv')
year_dict = {}

electronic = 0
paper = 0

with open(the_file, 'r') as incsv:
    datarows = list(csv.DictReader(incsv))

for row in datarows:
    #Count indivs per year
    year = re.findall('\d\d\d\d',row['Breach Submission Date'])[0]

    if not year_dict.get(year):
        year_dict[year] = 0 
        if not row['Individuals Affected'] == '':
            year_dict[year] += int(row['Individuals Affected'])
    else:
        if not row['Individuals Affected'] == '':
            year_dict[year] += int(row['Individuals Affected'])

    #Count total individuals affected
    if not row['Individuals Affected'] == '':
        indiv_affected += int(row['Individuals Affected'])

    if row['Location of Breached Information'] in ['Other', 'Other, Paper/Films', 'Paper/Films']:
        paper += 1

    else:
        electronic += 1

print(round(indiv_affected / 1000000, 1), 'million individuals have been affected')
print('There have been', paper, 'leaks of paper data')
print('There have been', electronic, 'leaks of electronic data')


#write csv for charti
with open('chart.csv', 'w') as fout:
    writer = csv.writer(fout)

    for y in year_dict:
        writer.writerow([y, year_dict[y]])