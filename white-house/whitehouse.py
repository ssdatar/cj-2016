from os.path import join
from os import makedirs
import bs4
from glob import glob
from urllib.parse import urljoin
import requests

# This script scrapes each page and extracts the URL for the briefing,
# and then scrapes the page for the briefing to get the briefing text.

index = 'white-house/index-pages'
base_url = 'https://www.whitehouse.gov/briefing-room/press-briefings/'
filenames = glob(join(index, '*.html'))
briefs_folder = 'briefs'
makedirs(briefs_folder, exist_ok=True)

for f in filenames:
	with open(f, 'r') as f_in:
		txt = f_in.read()
		soup = bs4.BeautifulSoup(txt, 'lxml')

		for title in soup.find_all('h3'):
			link = title.find('a').attrs['href']
			url = urljoin(base_url, link)
			resp = requests.get(url)

			given_name = link.replace('/', '-').strip('-')
			given_name = given_name + '.html'
			full_name = join(briefs_folder,given_name)
			print('Saving brief to: ', full_name)

			with open(full_name, 'w') as f_out:
				f_out.write(resp.text)