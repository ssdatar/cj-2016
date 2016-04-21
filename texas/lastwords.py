import requests
from bs4 import BeautifulSoup
from os.path import join, basename
from os import makedirs
from urllib.parse import urljoin
from glob import glob
import re

folder_path = join('pages', '*.html')

files = glob(folder_path)

master = {}

for f in files:
    last_words = ''
    print('Currently reading:', f)

    with open(f, 'r') as f_in:
        txt = f_in.read()
        soup = BeautifulSoup(txt, 'lxml')
        # CSS select last words and take text from last paragraph
        # Last words are always the last para on the page
        all_p = soup.select('p')

        for i in range(len(all_p)):
            if 'Offender:' in all_p[i].text:                
                offender = re.findall('\w+', all_p[i+1].text)
                if len(offender) < 3:
                    name = ' '.join(offender)
                else:
                    name = ' '.join(offender[:-1])
            
            if 'Last Statement:' in all_p[i]:
                last = all_p[i+1:]
            # print(last)

        if len(last) > 1:
            for l in last:
                last_words += l.text.strip()
        else:
                last_words = last[0].text.strip()
        # print('Got last words for:', name)

    if not master.get(name):
        master[name] = ''
    master[name] = last_words

religion_words = ['pray','holy spirit', 'God', 'Lord', 'Christ(?:ian\w*|mas)?', 'Islam', 'bless\w*','heaven', 'creator', 'Allah', 'M[uo]hamm[ea]d', 'Jesus', 'Bible', 'Scriptures','Koran', 'shepherd', 'Quran', 'Krishna', 'Buddha', 'Gospel']

non_relig = []

relegex = re.compile('(%s)' % '|'.join(religion_words), re.IGNORECASE)

for off in master:
    holy = relegex.findall(master[off]) 

    if not holy:
        non_relig.append(off)
        print(off, 'did not say anything related to religion.\n')
print(len(non_relig), 'people did not say any religious last words.')