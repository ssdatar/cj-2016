import os
import shutil
import requests

for year in range(2003, 2016):
    url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/' + str(year) + '_sqf_csv.zip'
    resp = requests.get(url)
    print('Downloading:', url)

    filename = os.path.join(str(year) + '-frisk.zip')

    with open(filename, 'wb') as fopen:
        print('Writing to:', filename)
        fopen.write(resp.content)

    shutil.unpack_archive(filename)