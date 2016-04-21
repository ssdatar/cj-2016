import requests
import os

# This script gets all the web pages containing a list of press briefings of the white house

url = 'https://www.whitehouse.gov/briefing-room/press-briefings'
last_page = 162
index = 'index-pages'
os.makedirs(index, exist_ok=True)

for pagenum in range(0, last_page):
    resp = requests.get(url, params={'page': pagenum})
    print("Downloaded", resp.url)

    the_file = os.path.join(index, '{}.html'.format(pagenum))
    print("Saving to", the_file)
    
    with open(the_file, 'w') as f_out:
        f_out.write(resp.text)