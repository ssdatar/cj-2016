import re
from os.path import join
from glob import glob

briefs_folder = 'briefs'

destination = join(briefs_folder, '*.html')
all_files = glob(destination)

isis = []

for f in all_files:
	with open(f, 'r') as f_in:
		txt = f_in.read()
		txt = txt.upper()
		
		if re.search(r'\bISI[LS]\b', txt):
			print(f, 'mentions ISIS/ISIL')
			isis.append(f)

#First element corresponds to first mention of isis
first = re.findall('\d+-', isis[0])
first = ''.join(first)[:-1] #Drop last '-' character
print('The first mention of ISIS/ISIL was on', first, '. It was an ISIL mention.')