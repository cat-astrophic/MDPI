# This script creates an interaction matrix for collaborating nations using the MDPI data

# To do this, quite a bit of cleaning has to occur first

# Importing required modules

import pandas as pd
import numpy as np

# A data cleaning function -- isolates the country name

def clean(s):
    
    x = 1
    
    while x > 0:
        
        s = s[x+2:]
        x = s.find(',')
    
    return s

# The main function
    
def main(rep):
    
    # Reading in the data
    
    data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/MDPIpapers_' + str(rep) + '.csv')
    
    # Cleaning the affiliation data (replace each list with a list of countries)
    
    Countries = []
    
    for item in data.Affiliations:
        
        temp = []
        idx = item.find("',")
    
        while idx > 0:
    
            s = item[:idx]
            item = item[idx+1:]
            
            # Ensuring no non-empty entries exist
            
            if (len(s) > 1):
                                    
                s = clean(s)
                temp.append(s)
            
            idx = item.find("',")
    
        if len(item[:len(item)-1]) > 1:

            item = clean(item[:len(item)-2])
            temp.append(item)
        
        Countries.append(temp)
    
    # Standardizing country names with a reference table
    
    # Countries are, when appropriate, in reverse alphabetical order in order to prevent false subset issues
    
    reference = {'Afghan': 'Afghanistan', 'Albania': 'Albania', 'Algeria': 'Algeria', 'Andorra': 'Andorra',
             'Angola': 'Angola', 'Antigua': 'Antigua and Barbuda', 'Argentin': 'Argentina', 'Armenia': 'Armenia',
             'Australia': 'Australia', 'Austri': 'Austria', 'Azerbaijan': 'Azerbaijan', 'Bahrain': 'Bahrain',
             'Bangladesh': 'Bangladesh', 'Barbados': 'Barbados', 'Belarus': 'Belarus', 'Belgium': 'Belgium',
             'Belize': 'Belize', 'Benin': 'Benin', 'Bolivia': 'Bolivia', 'Bosnia': 'Bosnia and Herzegovina',
             'Botswana': 'Botswana', 'Brazi': 'Brazil', 'Brunei': 'Brunei', 'Bulgaria': 'Bulgaria',
             'Burkina Faso': 'Burkina Faso', 'Burma': 'Burma', 'Burundi': 'Burundi', 'Cabo Verde': 'Cabo Verde',
             'Cambodia': 'Cambodia', 'Cameroon': 'Cameroon', 'Canada': 'Canada', 'Cape Verd': 'Cabo Verde',
             'Central African': 'Central African Republic', 'Chad': 'Chad', 'Chile': 'Chile', 'China': 'China',
             'Colombia': 'Colombia', 'Comoros': 'Comoros', 'Costa Rica': 'Costa Rica', 'Ivory Coast': 'Ivory Coast',
             "d’Iv": 'Ivory Coast', "D’Iv": 'Ivory Coast', 'Croatia': 'Croatia', 'Cuba': 'Cuba', 'Cyprus': 'Cyprus',
             'Czec': 'Czech Republic', 'Democratic Republic of the Congo': 'Democratic Republic of the Congo',
             'Congo (RDC': 'Democratic Republic of the Congo', 'DR Congo': 'Democratic Republic of the Congo',
             'Dem. Congo': 'Democratic Republic of the Congo', 'Cyrpus': 'Cyprus',
             'ocratic Republic of Congo': 'Democratic Republic of the Congo',
             'ocratic Republic of the Congo': 'Democratic Republic of the Congo',
             'du Congo': 'Democratic Republic of the Congo', 'Denmark': 'Denmark', 'Djibouti': 'Djibouti',
             'Dominican Republic': 'Dominican Republic', 'Dominica': 'Dominica', 'Ecuador': 'Ecuador',
             'Egypt': 'Egypt', 'El Salvador': 'El Salvador', 'Equatorial Guinea': 'Equatorial Guinea',
             'Eritrea': 'Eritrea', 'Estonia': 'Estonia', 'Eswatini': 'Eswatini', 'Ethiopia': 'Ethiopia',
             'Fiji': 'Fiji', 'Finland': 'Finland', 'France': 'France', 'Gabon': 'Gabon', 'Georgia': 'Georgia',
             'German': 'Germany', 'Ghana': 'Ghana', 'Greece': 'Greece', 'Grenada': 'Grenada',
             'Guatemala': 'Guatemala', 'Guinea-Bissau': 'Guinea-Bissau', 'Guinea': 'Guinea', 'Guyana': 'Guyana',
             'Haiti': 'Haiti', 'Honduras': 'Honduras', 'Hungary': 'Hungary', 'Iceland': 'Iceland', 'India': 'India',
             'Indonesia': 'Indonesia', 'Iran': 'Iran', 'Iraq': 'Iraq', 'Ireland': 'Ireland', 'Israel': 'Israel',
             'Italy': 'Italy', 'Jamaica': 'Jamaica', 'Japan': 'Japan', 'Jordan': 'Jordan',
             'Kazakhstan': 'Kazakhstan', 'Kenya': 'Kenya', 'Kiribati': 'Kiribati', 'Korea': 'Korea',
             'Kosovo': 'Kosovo', 'Kuwait': 'Kuwait', 'Kyrgyz': 'Kyrgyzstan', 'Lao': 'Laos', 'Latvia': 'Latvia',
             'Lebanon': 'Lebanon', 'Lesotho': 'Lesotho', 'Liberia': 'Liberia', 'Libya': 'Libya',
             'Liechtenstein': 'Liechtenstein', 'Lithuania': 'Lithuania', 'Luxembourg': 'Luxembourg',
             'Macedonia': 'Macedonia', 'Madagascar': 'Madagascar', 'Malawi': 'Malawi', 'Malaysia': 'Malaysia',
             'Maldives': 'Maldives', 'Mali': 'Mali', 'Malta': 'Malta', 'Marshall': 'Marshall Islands',
             'Mauritania': 'Mauritania', 'Mauritius': 'Mauritius', 'Mexico': 'Mexico', 'Micronesia': 'Micronesia',
             'Moldova': 'Moldova', 'Monaco': 'Monaco', 'Mongolia': 'Mongolia', 'Montenegro': 'Montenegro',
             'Morocco': 'Morocco', 'Mozambique': 'Mozambique', 'Namibia': 'Namibia', 'Nauru': 'Nauru',
             'Nepal': 'Nepal', 'Zealand': 'New Zealand', 'Nicaragua': 'Nicaragua', 'Nigeria': 'Nigeria',
             'Niger': 'Niger', 'Norway': 'Norway', 'Oman': 'Oman', 'Pakistan': 'Pakistan', 'Palau': 'Palau',
             'Panama': 'Panama', 'Papua': 'Papua New Guinea', 'Paraguay': 'Paraguay', 'Peru': 'Peru',
             'Philippines': 'Philippines', 'Poland': 'Poland', 'Portugal': 'Portugal', 'Qatar': 'Qatar',
             'Congo': 'Republic of the Congo', 'Romania': 'Romania', 'Russia': 'Russia', 'Rwanda': 'Rwanda',
             'Kitts': 'Saint Kitts and Nevis', 'Lucia': 'Saint Lucia', 'Vincent': 'Saint Vincent and the Grenadines',
             'Samoa': 'Samoa', 'Marino': 'San Marino', 'Principe': 'Sao Tome and Principe', 'Arabia': 'Saudi Arabia',
             'Senegal': 'Senegal', 'Serbia': 'Serbia', 'Seychelles': 'Seychelles', 'Leone': 'Sierra Leone',
             'Singapore': 'Singapore', 'Slovak': 'Slovakia', 'Slovenia': 'Slovenia', 'Somalia': 'Somalia',
             'South Africa': 'South Africa', 'South Sudan': 'South Sudan', 'Spain': 'Spain',
             'Sri Lanka': 'Sri Lanka', 'Sudan': 'Sudan', 'Suriname': 'Suriname', 'Sweden': 'Sweden',
             'Switzerland': 'Switzerland', 'Syria': 'Syria', 'Tajikistan': 'Tajikistan', 'Tanzania': 'Tanzania',
             'Thailand': 'Thailand', 'Bahamas': 'The Bahamas', 'Cayman': 'The Cayman Islands',
             'Gambia': 'The Gambia', 'Nether': 'The Netherlands', 'Soloman': 'The Solomon Islands',
             'Timor': 'Timor-Leste', 'Togo': 'Togo', 'Tonga': 'Tonga', 'Trinidad': 'Trinidad and Tobago',
             'Tunisia': 'Tunisia', 'Turkey': 'Turkey', 'Turkmenistan': 'Turkmenistan', 'Tuvalu': 'Tuvalu',
             'Uganda': 'Uganda', 'UK': 'UK', 'Ukraine': 'Ukraine', 'United Arab Emirates': 'United Arab Emirates',
             'UAE': 'United Arab Emirates', 'Uruguay': 'Uruguay', 'USA': 'USA', 'Uzbekistan': 'Uzbekistan',
             'Vanuatu': 'Vanuatu', 'Venezuela': 'Venezuela', 'Vietnam': 'Vietnam', 'Yemen': 'Yemen',
             'Zambia': 'Zambia', 'Zimbabwe': 'Zimbabwe', 'china': 'China', 'España': 'Spain', 'INDIA': 'India',
             'Viet Nam': 'Vietnam', 'Viet-Nam': 'Vietnam', 'VietNam': 'Vietnam', 'México': 'Mexico',
             'AUSTRIA': 'Austria', 'AZERBAIJAN': 'Azerbaijan', 'Albnia': 'Albania', 'Alegria': 'Algeria',
             'Algeria': 'Algeria', 'Algerie': 'Algeria', 'Algérie': 'Algeria', 'Banglasesh': 'Bangladesh',
             'BELGIUM': 'Belgium', 'Belgique': 'Belgium', 'Belium': 'Belgium', 'Bosna i': 'Bosnia and Herzegovina',
             'Brasil': 'Brazil', 'Bénin': 'Benin', 'Check Republic': 'Czech Republic', 'Taiwan': 'Taiwan',
             'Chlie': 'Chile', 'Chin': 'China', 'Columbia': 'Colombia', 'Demark': 'Denmark', 'Danemark': 'Denmark',
             'Danmark': 'Denmark', 'Deutschland': 'Germany', 'EGYPT': 'Egypt', 'Espana': 'Spain', 'FRANCE': 'France',
             'FINLAND': 'Finland', 'FInland': 'Finland', 'Gemany': 'Germany', 'Germnay': 'Germany', 'Haïti': 'Haiti',
             'Hong Kong': 'Hong Kong', 'ITALY': 'Italy', 'Iatly': 'Italy', 'Irenland': 'Ireland', 'Italia': 'Italy',
             'Itlay': 'Italy', 'Irak': 'Iraq', 'Iraki': 'Iraq', 'JAPAN': 'Japan', 'KSA': 'Saudi Arabia',
             'Kazakistan': 'Kazakhstan', 'Koera': 'Korea', 'Kosova': 'Kosovo', 'Lithiuania': 'Lithuania',
             'Lithunia': 'Lithuania', 'Luxemburg': 'Luxembourg', 'U.S.A': 'USA', 'Maroc': 'Morocco',
             'Morroco': 'Morocco', 'Moçambique': 'Mozambique', 'Panamá': 'Panama', 'Palestine': 'Palestine',
             'Јapan': 'Japan', 'witzerland': 'Switzerland', 'zech Republic': 'Czech Republic', 'urkey': 'Turkey',
             'ussia': 'Russia', 'ustralia': 'Australia', 'ustria': 'Austria', 'United Kingdom': 'UK',
             'roatia': 'Croatia', 'reece': 'Greece', 'rance': 'France', 'razil': 'Brazil', 'orway': 'Norway',
             'outh Africa': 'South Africa', 'olombia': 'Colombia', 'omânia': 'Romania', 'lovenia': 'Slovenia',
             'korea': 'Korea', 'ietnam': 'Vietnam', 'ermany': 'Germany', 'erbia': 'Serbia', 'exico': 'Mexico',
             'elgium': 'Belgium', 'emezuela': 'Venezuela', 'enmark': 'Denmark', 'angladesh': 'Bangladesh',
             'apan': 'Japan', 'anada': 'Canada', 'anama': 'Panama', 'alaysia': 'Malaysia', 'ameroon': 'Cameroon',
             'aiwan': 'Taiwan', 'United States': 'USA', 'UNITED KINGDOM': 'UK', 'U.K': 'UK',
             'United Arab Emirate': 'United Arab Emirates', 'U.A.E': 'United Arab Emirates', 'U.S': 'USA',
             'Tunisie': 'Tunisia', 'Tunisa': 'Tunisia', 'Turkiye': 'Turkey', 'Türkei': 'Turkey', 'Türkiye': 'Turkey',
             'Nederland': 'The Netherlands', 'Switzland': 'Switzerland', 'Switerland': 'Switzerland',
             'Switzerlan': 'Switzerland', 'Sénégal': 'Senegal', 'Sri-Lanka': 'Sri Lanka', 'Slovenija': 'Slovenia',
             'Slovenja': 'Slovenia', 'Slovac': 'Slovakia', 'Singpore': 'Singapore', 'Scotland': 'UK',
             'Sapin': 'Spain', 'Saudi Ardbia': 'Saudi Arabia', 'Saudia Arabia': 'Saudi Arabia', 'Puerto Rico': 'USA',
             'SPAIN': 'Spain', 'România': 'Romania', 'Perú': 'Peru', 'KOREA': 'Korea', 'TURKEY': 'Turkey',
             'enezuela': 'Venezuela', 'ndia': 'India', 'hina': 'China', 'ingapore': 'Singapore', 'Zimbawe': 'Zimbabwe',
             'Cote': 'Ivory Coast', 'Cameroun': 'Cameroon', 'South Arica': 'South Africa', 'England': 'UK',
             'Czech Republic': 'Czech Republic', 'Great Britain': 'UK', 'Gremany': 'Germany', 'Marroco': 'Morocco',
             'Morocoo': 'Morocco', 'Potugal': 'Portugal', 'Swaziland': 'Eswatini', 'orea': 'Korea', 'pain': 'Spain',
             'rgentina': 'Argentina', 'taly': 'Italy', 'Moroc': 'Morocco'}
    
    refs = [*reference.values()]
    
    # Clean values by using the dictionary values
    
    for i in range(len(Countries)):
    
        for j in range(len(Countries[i])):
                                       
            for ref in reference:
                
                if ref in str(Countries[i][j]):
                
                    Countries[i][j] = reference[ref]
                    
                    break
    
    # Removing everything that is not a dictionary value
    
    for i in range(len(Countries)):
        
        for j in range(len(Countries[i])):
            
            if Countries[i][j] not in refs:
                
                Countries[i][j] = 'DELETE'
    
        # Remove 'DELETE'
        
        length = len(Countries[i])
        count = 0
            
        while(count < length):
            
            if Countries[i][count] == 'DELETE':
            
                Countries[i].remove(Countries[i][count])
                length = length - 1
                
                continue
            
            count += 1
                
    # Make a list of unique countries collaborating on each paper
    
    Collaborators = [list(set(country)) for country in Countries]
    blank_collab_ids = [i for i in range(len(Collaborators)) if Collaborators[i] == []]
    
    for blank_id in [blank_collab_ids[len(blank_collab_ids)-i-1] for i in range(len(blank_collab_ids))]:
        
        Collaborators.pop(blank_id)
    
    # Create interaction matrix
    
    # First, create a referene table
    
    reftab = sorted(list(set([country for collaboration in Collaborators for country in collaboration])))
    
    # Second, initialize the interaction matrix
    
    M = np.zeros((len(reftab),len(reftab)))
    
    # Third, complete the matrix and remove blank collaboration rows
    
    for collaboration in Collaborators:
        
        if len(collaboration) > 1:
            
            for i in range(len(collaboration)-1):
                
                for j in range(i+1,len(collaboration)):
                    
                    id1 = reftab.index(collaboration[i])
                    id2 = reftab.index(collaboration[j])
                    M[id1,id2] += 1
                    M[id2,id1] += 1
    
    # Save the interaction matrix and Collaborators list as csv files
    
    pd.DataFrame(M, columns = reftab).to_csv('C:/Users/User/Documents/Data/MDPI/M_' + str(rep) + '.csv', index = False)
    pd.DataFrame(Collaborators).to_csv('C:/Users/User/Documents/Data/MDPI/Collaborators_' + str(rep) + '.csv', index = False)

# Using the main function to get overall and annual results

repetitions = ['all', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
             '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

for rep in repetitions:

    main(rep)

