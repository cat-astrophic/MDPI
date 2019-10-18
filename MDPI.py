# This script gathers paper metadata from papers accepted at MDPI journals

# Importing required modules

import urllib
from bs4 import BeautifulSoup as bs

# Defining results pages from an empty search query (there are 19411 pages)

start = 'https://www.mdpi.com/search?sort=pubdate&page_no='
end = '&page_count=10&year_from=1996&year_to=2018&view=default'

# Scraping the metadata from all submissions

links = []

for i in range(19411):
    
    # Declaring which results page from the empty search query we want to scrape
    
    url = start + str(i+1) + end
    print('Retrieving data from query page ' + str(i+1) + ' of 19411.')
    
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
        
with open('C:/Users/User/Documents/Data/MDPI/links.txt', 'a') as file:
    
    for link in links:
        
        file.write(str(link)+'\n')
    
    file.close()

