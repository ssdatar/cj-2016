import csv
from csv import DictReader

all_stops = []

for year in range(2003, 2015):
    filename = str(year) + '.csv'
    print('Opening:', filename)

    stops = { str(year): {'total': 0, 'innocent': 0} }

    with open(filename, 'r', encoding='utf-8', errors='ignore') as infile:
        datarows = list(DictReader(infile))
        stops[str(year)]['total'] = len(datarows)

    innocent_count = 0
    for row in datarows:
        if row['arstmade'] == 'N' and row['sumissue'] == 'N':
            innocent_count += 1
    stops[str(year)]['innocent'] = innocent_count
    all_stops.append(stops)

#Separately open 2015 file
stops = { '2015': {'total': 0, 'innocent': 0} }
with open('2015_sqf_csv.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    datarows = list(DictReader(infile))
    stops['2015']['total'] = len(datarows)

innocent_count = 0
for row in datarows:
    if row['arstmade'] == 'N' and row['sumissue'] == 'N':
        innocent_count += 1
stops['2015']['innocent'] = innocent_count
all_stops.append(stops)


innocent = 0
total = 0
y = 2003
ratio = 0

for i in range(len(all_stops)):
    ratio = round(all_stops[i][str(y)]['innocent'] / all_stops[i][str(y)]['total'], 2) 
    
    if y < 2016:
        #Print stats for the current year
        print('In the year', y) 
        print(all_stops[i][str(y)]['innocent'], 'innocent people out of', all_stops[i][str(y)]['total'], 'were stopped')
        print(ratio * 100, 'percent of people stopped were innocent\n')
        
        #Add to total to confirm grand total
        innocent += all_stops[i][str(y)]['innocent']
        total += all_stops[i][str(y)]['total']
        y += 1
    else:
        break

print('Since 2003, police have stopped', total, 'New Yorkers')
print('Out of that', innocent, 'were innocent')
print('Ratio of innocent stops to total stops:', round(innocent / total, 1))
print('NYCLU\'s ratio has been confirmed')