import pdfplumber
import glob
import requests
from os.path import basename
import csv

urls = [
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn13.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn14.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN_Interim_041614_to_063014.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARNReportfor7-1-2014to06-30-2015.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN-Report-for-7-1-2015-to-03-25-2016.pdf'
]

all_pdfs = glob.glob('CAWARN-*.pdf')

for url in urls:
    print(url)
    pdf_name = 'CAWARN-' + basename(url)
    print("Downloading", url, 'into', pdf_name)
    resp = requests.get(url)
    
    with open(pdf_name, 'wb') as fout:
        fout.write(resp.content)

def parse_old(page):
    table = page.extract_table()
    employees_affected = 0
    
    for row in table[1:]:
        employees_affected += int(row[2])
    return employees_affected

def parse_new(page):
    table = page.extract_table()
    employees_affected = 0

    for row in table[1:]:
        if not row[2]:
            employees_affected += int(row[5])

    return employees_affected

def write_to_csv(filename, data, index):
    with open(filename, 'w') as csvout:
        writer = csv.writer(csvout)

        if index == 4:
            for row in data:
                if row[4] is not None:
                    row[4] = (row[4]+row[5]+row[6]).replace(' ','')
                    row[5] = (row[8]+row[10]).replace(' ','')
                    row[6] = (row[12]+row[14]).replace(' ','')
                    writer.writerow([row[2],row[4],row[5],row[6],row[20],row[24,row[28],row[30]]])

        elif index > 2:
            for row in data:
                if row[4] is not None:
                    writer.writerow([row[2],row[4],row[6],row[8],row[10],row[12],row[14]])

        else:
            for row in data:
                writer.writerow(row)

jobs_lost = 0


#Loop through each PDF file
for index, doc in enumerate(all_pdfs):
    master_table = []
    pdf = pdfplumber.open(doc)
    fname = doc[:len(doc) - 3] + 'csv'

    # Check if this is the first of three files whose
    # format is the same. Otherwise, use other format
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        table = page.extract_table()

        for row in table:
            if index <= 2:
                master_table.append(row)

            elif index is not 4:
                if row[4] is not None:
                    master_table.append(row)

    write_to_csv(fname, master_table, index)


#Had to do cleaning for this one
pdf2 = pdfplumber.open('CAWARN-WARN_Interim_041614_to_063014.pdf')
master_table2 = []
fname2 = 'CAWARN-WARN_Interim_041614_to_063014' + '.csv'

for i in range(len(pdf2.pages)):
    page2 = pdf2.pages[i]
    table2 = page2.extract_table()

    for item in table2:
        master_table2.append(item)

ar = []
for k in range(2,len(master_table2),3):
    ar.append(master_table2[k])


with open(fname2, 'w') as fout2:
    writer2 = csv.writer(fout2)

    for datarow in ar:
        # d = [datarow[0],datarow[1],datarow[2],datarow[3],datarow[4],datarow[7],datarow[11]]
        writer2.writerow(datarow)