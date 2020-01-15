# This script gathers the data of interest for the MDPI project

# Importing required modules

import pandas as pd
import urllib
from bs4 import BeautifulSoup as bs

# Get links from previous output file

file = open('C:/Users/User/Documents/Data/MDPI/links.txt', 'r')
links = file.readlines()
file.close()

# A function used to help parse strings

def affiliation_finder(string):
    
    return any(s.isdigit() for s in string)

# Go to each links and extract the desired data

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

MDPI_df = pd.DataFrame({'Year': years, 'Journal': journals, 'Affiliations': affiliations})
MDPI_df.to_csv('C:/Users/User/Documents/Data/MDPI/MDPIpapers_all.csv', index = False, encoding = 'utf-8-sig')
