import requests
import csv
from bs4 import BeautifulSoup

#Find table and save content in CSV function
def getTableInCsv(link,csvfile,index):

    #Grab content
    result = requests.get(link)

    #Save source in variable
    source = result.content

    #Activate soup
    soup = BeautifulSoup(source,'lxml')
    
    #Find all tables 
    findtable = soup.find_all('table')

    #Find specific table with index
    findtable2 = findtable[index]
        
    #Open csv and save table
    with open (csvfile,'w',encoding='utf-8',newline='')as f:
        writer = csv.writer(f)
        for x in findtable2('tr'):
            row = [t.get_text(strip=True)for t in x (['td','th'])]
            writer.writerow(row)
        
#Link, CSV file name and index of table to scrape
getTableInCsv('https://en.wikipedia.org/wiki/List_of_countries_by_tax_rates','countriestaxrate.csv',9) 
getTableInCsv('https://en.wikipedia.org/wiki/List_of_countries_by_tax_revenue_to_GDP_ratio','countriesgdprevenue.csv',6)
getTableInCsv('https://en.wikipedia.org/wiki/Tax_evasion_in_the_United_States','unitedstatestaxevasion.csv',1)

############################################CSV clean up###############################################

#Tax rate by country
#Open csv file and read
with open ('countriestaxrate.csv') as inf:
    reader = csv.reader(inf.readlines()[1:])

with open ('countriestaxrate.csv','w',newline='') as outf:
    writer =csv.writer(outf)
    writer.writerow(('Country','Corporate tax','Income Tax(lowest marginal rate)','Income Tax(highest marginal rate)'))
    blocker = list(range(0,101))
    for numb in blocker:
        numb = str([numb])
    for line in reader:
        cell1 = line[0]
        cell2 = line[1][:2].replace('%','').replace('N/','0').replace('.','').replace('mi','')
        cell3 = line[2][:2].replace('%','').replace('N/','0').replace('.','').replace('mi','')
        cell4 = line[3][:2].replace('%','').replace('N/','0').replace('.','').replace('mi','')
        row = [cell1,cell2,cell3,cell4]
        writer.writerow(row)

#----------------------------------------------------------------------------------------------------#

##Tax revenue to GDP ratio by country##
#Open csv file and read
with open('countriesgdprevenue.csv') as inf:
    reader = csv.reader(inf.readlines()[1:])

#Open csv file and overwrite
with open('countriesgdprevenue.csv','w',newline='') as outf:
    writer = csv.writer(outf)
    writer.writerow(('Country','Tax as % of GDP'))
    for line in reader:
        cell1 = line[0].replace(',','')
        cell2 = line[1][:4]
        row = [cell1,cell2]
        writer.writerow(row)

#----------------------------------------------------------------------------------------------------#

##Tax evasion United states
#Open csv file and read
with open('unitedstatestaxevasion.csv') as inf:
    reader = csv.reader(inf.readlines()[1:-2])

#Open csv file and overwrite
with open('unitedstatestaxevasion.csv','w',newline='') as outf:
    writer = csv.writer(outf)
    writer.writerow(('Year','Revenue Lost (US$ Billion)'))
    for line in reader:
        cell1 = line[0]
        cell2 = line[1][:3]
        row = [cell1,cell2]
        writer.writerow(row)

#----------------------------------------------------------------------------------------------------#


