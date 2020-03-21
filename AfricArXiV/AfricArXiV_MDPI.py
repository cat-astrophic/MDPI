# This script is for the AfricArXiV search portal

# Importing required modules

import pandas as pd
import numpy as np
import urllib
from bs4 import BeautifulSoup as bs

# Search query results page

url1 = 'https://www.mdpi.com/search?sort=pubdate&page_count=10&featured=&subjects=&journals=&article_types=&countries=EGYPT%2CSOUTH_AFRICA%2CNIGERIA%2CMOROCCO%2CTUNISIA%2CKENYA%2CALGERIA%2CGHANA%2CETHIOPIA%2CTANZANIA_UNITED_REPUBLIC_OF%2CCAMEROON%2CUGANDA%2CSUDAN%2CSENEGAL%2CBENIN%2CBURKINA_FASO%2CMALAWI%2CZAMBIA%2CLIBYAN_ARAB_JAMAHIRIYA%2CZIMBABWE%2CRWANDA%2CMALI%2CBOTSWANA%2CMOZAMBIQUE%2CMADAGASCAR%2CCOTE_DIVOIRE%2CMAURITIUS%2CNAMIBIA%2CNIGER%2CCONGO%2CSIERRA_LEONE%2CSWAZILAND%2CGABON%2CANGOLA%2CBURUNDI%2CGUINEA%2CCAPE_VERDE%2CMAURITANIA%2CCOMOROS%2CERITREA%2CSEYCHELLES%2CGAMBIA%2CLIBERIA%2CCHAD%2CLESOTHO%2CCENTRAL_AFRICAN_REPUBLIC%2CCONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE%2CGUINEA-BISSAU%2CSOMALIA'
start = 'https://www.mdpi.com/search?sort=pubdate&page_no='
end = '&page_count=10&featured=&subjects=&journals=&article_types=&countries=EGYPT%2CSOUTH_AFRICA%2CNIGERIA%2CMOROCCO%2CTUNISIA%2CKENYA%2CALGERIA%2CGHANA%2CETHIOPIA%2CTANZANIA_UNITED_REPUBLIC_OF%2CCAMEROON%2CUGANDA%2CSUDAN%2CSENEGAL%2CBENIN%2CBURKINA_FASO%2CMALAWI%2CZAMBIA%2CLIBYAN_ARAB_JAMAHIRIYA%2CZIMBABWE%2CRWANDA%2CMALI%2CBOTSWANA%2CMOZAMBIQUE%2CMADAGASCAR%2CCOTE_DIVOIRE%2CMAURITIUS%2CNAMIBIA%2CNIGER%2CCONGO%2CSIERRA_LEONE%2CSWAZILAND%2CGABON%2CANGOLA%2CBURUNDI%2CGUINEA%2CCAPE_VERDE%2CMAURITANIA%2CCOMOROS%2CERITREA%2CSEYCHELLES%2CGAMBIA%2CLIBERIA%2CCHAD%2CLESOTHO%2CCENTRAL_AFRICAN_REPUBLIC%2CCONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE%2CGUINEA-BISSAU%2CSOMALIA'

# First determine how many results and results pages there are

page = urllib.request.Request(url1, headers = {'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(page)
soup = bs(response, 'html.parser')
findit = soup.find_all('h1')
a = str(findit[0]).find('(')
b = str(findit[0]).find(')')
papers = int(str(findit[0])[a+1:b])
length = int(np.ceil(papers/10))

# Building and running the scraper

links = []

for i in range(length):
    
    # Declaring which results page from the empty search query we want to scrape
    
    url = start + str(i+1) + end
    print('Retrieving data from query page ' + str(i+1) + ' of ' + str(length) + '.')
    
    # Getting the raw data
    
    try:
        
        page = urllib.request.Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(page)
        soup = bs(response, 'html.parser')
        
        # Making a list of the paper links from that results page
        
        data = soup.find_all('a')
        articles = []
        
        for dat in data:
            
            if str(dat)[0:21] == '<a class="title-link"':
                
                articles.append(dat)
        
        for art in articles:
            
            c1 = str(art).find('href="')
            c2 = str(art)[c1+6:].find('"')
            links.append('https://www.mdpi.com' + str(art)[c1+6:c1+6+c2])
        
    except:
        
        continue

# Write links to file
        
with open('C:/Users/User/Documents/Data/MDPI/AfricArXiV/links.txt', 'w') as file:
    
    for link in links:
        
        file.write(str(link)+'\n')
    
    file.close()

# A function used to help parse strings

def affiliation_finder(string):
    
    return any(s.isdigit() for s in string)

# Go to each link and extract the desired data

affiliations = []
journals = []
years = []

for link in links:
    
    try:
        
        print('Retrieving data from link #' + str(links.index(link)+1) + ' of ' + str(len(links)))
        page = urllib.request.Request(link[:len(link)-1], headers = {'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(page)
        soup = bs(response, 'html.parser')
        data = soup.find_all('div')
        paper_affiliations = []
        bib_journals = []
        bib_years = []
        temp_affs = []

        for dat in data:

            if str(dat)[0:28] == '<div class="affiliation-name':

                paper_affiliations.append(dat)

            if str(dat)[0:25] == '<div class="bib-identity"':

                bib_journals.append(dat)

            if str(dat)[0:23] == '<div class="pubhistory"':

                bib_years.append(dat)

        for aff in paper_affiliations:

            c1 = str(aff).find('>')
            c2 = str(aff)[c1+1:].find('<')
            s = str(aff)[c1+1:c1+c2+1]

            if affiliation_finder(str(aff)) is True:

                temp_affs.append(s)

        if len(temp_affs) > 0:

            affiliations.append(temp_affs)

            for bib in bib_journals:

                yr1 = str(bib).find('<em>')
                yr2 = str(bib)[yr1+4:].find('</em>')
                journals.append(str(bib)[yr1+4:yr1+yr2+4])

            for bib in bib_years:

                j1 = str(bib).find('Published: ')
                j2 = str(bib)[j1+11:].find('<')        
                years.append(str(bib)[j1+j2+6:j1+j2+10])
            
    except:
        
        continue

# Create dataframe of all results and save a copy

MDPI_df = pd.DataFrame({'Year': years, 'Journal': journals, 'Affiliations': affiliations})
MDPI_df.to_csv('C:/Users/User/Documents/Data/MDPI/MDPIpapers_all.csv', index = False, encoding = 'utf-8-sig')

