import requests
from bs4 import BeautifulSoup
from os.path import join, basename
from os import makedirs
from urllib.parse import urljoin

index_url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
makedirs('pages',exist_ok=True)
index_name = basename(index_page)
col_no = 2

def get_index(url):
    resp = requests.get(url)
    txt = resp.text

    with open(index_name, 'w') as w:
        w.write(txt)

get_index(index_url)

# Download all pages
with open(index_name, 'r') as f:
    txt = f.read()
    soup = BeautifulSoup(txt, 'lxml')
    rows = soup.find_all('tr')

    for row in rows:
        print(row)
        if '</th>' not in str(row):
            last = row.find_all('td')[col_no]
            link = last.find('a').attrs['href']

            if 'no_last_statement' not in link:
                url = urljoin(index_url, link)
                print('Downloading:', url)
                r = requests.get(url)

                with open('pages/' + basename(url), 'w') as f_out:
                    f_out.write(r.text)