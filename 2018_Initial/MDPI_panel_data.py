# This script creates a panel data set

# Importing required modules

import pandas as pd
import numpy as np

# Create data frames for regression analyses

reps = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
        '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

# Create a lists of nations by year and their respective number of MDPI publications

nations = [] # Reference for nation
collaborators = [] # Total number of collaborators over all papers that year
collaborations = [] # Number of papers with at least one other nation represented
mean_collaborators = [] # Mean number of international collaborators per paper for each year (does not include base nation)
collab_ratio = [] # Proportion of papers that year which include at least one other nation
years = [] # Reference for year
pubs = [] # Total number of publications that year (in MDPI journals)
all_pubs = [] # Total number of publications that year in all (indexed) journals -- not only OA journals!
citations = [] # Total citations of papers with authors from given country
self_citations = [] # Total self-citations
self_cite_ratio = [] # Ratio of self-citations to total citations
citations_per_doc = [] # Citations per paper
h_index = [] # H index

for rep in reps:
    print(rep)
    # Collaborators data
    
    M = pd.read_csv('C:/Users/User/Documents/Data/MDPI/M_' + rep + '.csv')
    
    for country in M.columns:
        
        nations.append(country)
        collaborators.append(sum(M[country]))
        years.append(int(rep))
    
    # Publications and collaborations data
    
    data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/Collaborators_' + rep + '.csv').values
    scimago = pd.read_csv('C:/Users/User/Documents/Data/MDPI/scimagojr_' + rep + '.csv')
    
    for nation in M.columns:
        
        count = 0
        count2 = 0
    
        for i in range(len(data)):
            
            for j in range(len(data[i])):
                
                if data[i][j] == nation:
                    
                    count += 1
                    
                    if len(data[i]) > 1:
                        
                        count2 += 1
            
        pubs.append(count)
        collaborations.append(count2)
        mean_collaborators.append(collaborators[-1]/count2)
        collab_ratio.append(count2/count)
        
        try:
        
            idx = scimago[scimago['Country'] == nation].index[0]
            all_pubs.append(scimago['Citable documents'][idx])
            citations.append(scimago['Citations'][idx])
            self_citations.append(scimago['Self-citations'][idx])
            self_cite_ratio.append(scimago['Self-citations'][idx]/scimago['Citations'][idx])
            citations_per_doc.append(scimago['Citations per document'][idx])
            h_index.append(scimago['H index'][idx])

        except:
            
            all_pubs.append('nan')
            citations.append('nan')
            self_citations.append('nan')
            self_cite_ratio.append('nan')
            citations_per_doc.append('nan')
            h_index.append('nan')
            
    
# Build GDP per capita and population data

gdp_data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/gdp_data.csv').set_index('Country')
pop_data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/pop_data.csv').set_index('Country')
gdp = [] # GDP per capita data
pop = [] # Population data

for i in range(len(nations)):
    
    gdp.append(gdp_data[str(years[i])][nations[i]])
    pop.append(pop_data[str(years[i])][nations[i]])

ln_gdp = [np.log(g) for g in gdp]

# Collaborations and publications per capita data (per million people)

collaborations_per_cap = []
pubs_per_cap = []
all_pubs_per_cap = []

for i in range(len(nations)):
    
    if pop[i] != 'nan':
    
        collaborations_per_cap.append((1000000*collaborations[i])/pop[i])
        pubs_per_cap.append((1000000*pubs[i])/pop[i])
        
        if all_pubs[i] != 'nan':
        
            all_pubs_per_cap.append(1000000*all_pubs[i]/pop[i])
            
        else:
            
            all_pubs_per_cap.append('nan')
        
    else:
        
        collaborations_per_cap.append('nan')
        pubs_per_cap.append('nan')
        all_pubs_per_cap.append('nan')

# Create dataframe and save as csv

nations = pd.DataFrame(nations, columns = ['Nation'])
years = pd.DataFrame(years, columns = ['Year'])
pubs = pd.DataFrame(pubs, columns = ['Publications'])
collaborations = pd.DataFrame(collaborations, columns = ['Collaborations'])
collaborators = pd.DataFrame(collaborators, columns = ['Collaborators'])
gdp = pd.DataFrame(gdp, columns = ['GDP_per_capita'])
ln_gdp = pd.DataFrame(ln_gdp, columns = ['GDP_per_capita_ln'])
pop = pd.DataFrame(pop, columns = ['Population'])
pubs_per_cap = pd.DataFrame(pubs_per_cap, columns = ['Pubs_per_capita'])
collaborations_per_cap = pd.DataFrame(collaborations_per_cap, columns = ['Collabs_per_capita'])
mean_collaborators = pd.DataFrame(mean_collaborators, columns = ['Mean_Collaborators'])
collab_ratio = pd.DataFrame(collab_ratio, columns = ['Collaboration_Ratio'])
all_pubs = pd.DataFrame(all_pubs, columns = ['Total_Publications'])
citations = pd.DataFrame(citations, columns = ['Total_Citations'])
self_citations = pd.DataFrame(self_citations, columns = ['Self_Citations'])
self_cite_ratio = pd.DataFrame(self_cite_ratio, columns = ['Self_Cite_Ratio'])
citations_per_doc = pd.DataFrame(citations_per_doc, columns = ['Citations_per_Pub'])
h_index = pd.DataFrame(h_index, columns = ['H_Index'])
all_pubs_per_cap = pd.DataFrame(all_pubs_per_cap, columns = ['Total_Pubs_per_capita'])
df = pd.concat([nations, years, pubs, collaborations, collaborators, gdp, ln_gdp, pop, pubs_per_cap,
                collaborations_per_cap, mean_collaborators, collab_ratio, all_pubs, citations,
                self_citations, self_cite_ratio, citations_per_doc, h_index, all_pubs_per_cap], axis = 1)
df.to_csv('C:/Users/User/Documents/Data/MDPI/panel_data.csv', index = False)

