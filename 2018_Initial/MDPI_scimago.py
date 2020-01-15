# This script converts the names of countries in the scimagojr data to what is used in the MDPI data

# Scimago data was manually downloaded (invdividual file for each year plus one more for all years)

# Importing required modules

import pandas as pd

# Reference list for changing names

change = {'Viet Nam': 'Vietnam', 'United States': 'USA', 'United Kingdom': 'UK', 'Gambia': 'The Gambia',
          'Syrian Arab Republic': 'Syria',  'Bahamas': 'The Bahamas', 'Netherlands': 'The Netherlands',
          'Cayman Islands': 'The Cayman Islands', 'Russian Federation': 'Russia', 'Congo': 'Republic of the Congo',
          'Federated States of Micronesia': 'Micronesia', 'South Korea': 'Korea', 'Côte d’Ivoire': 'Ivory Coast',
          'Swaziland': 'Eswatini', 'Democratic Republic Congo': 'Democratic Republic of the Congo',
          'Brunei Darussalam': 'Brunei', 'Cape Verde': 'Cabo Verde'}

# Cleaning files

reps = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
        '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 'all']

for rep in reps:
    
    data = pd.read_excel('C:/Users/User/Documents/Data/MDPI/scimagojr_' + rep + '.xlsx')
    
    for country in data.Country:
        
        if country in change:
            
            idx = data[data['Country'] == country].index[0]
            data['Country'].iloc[idx] = change[country]
    
    data.to_csv('C:/Users/User/Documents/Data/MDPI/scimagojr_' + rep + '.csv', index = False)

