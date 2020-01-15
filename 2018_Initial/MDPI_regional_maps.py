# This script creates choropleths for the regional and income group of top collaborators

# Importing required modules

import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt

# Reading in the data

data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/M_all.csv')
data18 = pd.read_csv('C:/Users/User/Documents/Data/MDPI/M_2018.csv')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Creating regional dictionaries
    
Africa = {'Nigeria':'Nigeria', 'Ethiopia':'Ethiopia', 'Egypt':'Egypt', 'South Africa':'South Africa',
          'Democratic Republic of the Congo':'Dem. Rep. Congo', 'Tanzania':'Tanzania', 'Kenya':'Kenya',
          'Sudan':'Sudan', 'Algeria':'Algeria', 'Uganda':'Uganda', 'Morocco':'Morocco',
          'Mozambique':'Mozambique', 'Ghana':'Ghana', 'Angola':'Angola', 'Ivory Coast':"Côte d'Ivoire",
          'Madagascar':'Madagascar', 'Cameroon':'Cameroon', 'Niger':'Niger', 'Burkina Faso':'Burkina Faso',
          'Mali':'Mali', 'Malawi':'Malawi', 'Zambia':'Zambia', 'Somalia':'Somalia', 'Senegal':'Senegal',
          'Chad':'Chad', 'Zimbabwe':'Zimbabwe', 'Rwanda':'Rwanda', 'Tunisia':'Tunisia', 'Guinea':'Guinea',
          'Benin':'Benin', 'Burundi':'Burundi', 'South Sudan':'S. Sudan', 'Togo':'Togo',
          'Eritrea':'Eritrea', 'Sierra Leone':'Sierra Leone', 'Libya':'Libya', 'Namibia':'Namibia', 
          'Republic of the Congo':'Congo', 'Central African Republic':'Central African Rep.',
          'Liberia':'Liberia', 'Mauritania':'Mauritania', 'Botswana':'Botswana', 'Lesotho':'Lesotho',
          'The Gambia':'Gambia', 'Gabon':'Gabon', 'Guinea-Bissau':'Guinea-Bissau',
          'Equatorial Guinea':'Eq. Guinea', 'Eswatini':'Swaziland', 'Djibouti':'Djibouti', 'Western Sahara':'W. Sahara'}

Asia = {'Afghanistan':'Afghanistan', 'Armenia':'Armenia', 'Azerbaijan':'Azerbaijan',
        'Bangladesh':'Bangladesh', 'Bhutan':'Bhutan', 'Brunei':'Brunei', 'Myanmar':'Myanmar', 'Cambodia':'Cambodia',
        'China':'China', 'Georgia':'Georgia', 'India':'India', 'Indonesia':'Indonesia',
        'Iran':'Iran', 'Iraq':'Iraq', 'Israel':'Israel', 'Japan':'Japan', 'Jordan':'Jordan',
        'Kazakhstan':'Kazakhstan', 'Korea, Dem. Rep.':'Dem. Rep. Korea', 'Korea':'Korea', 'Kuwait':'Kuwait',
        'Kyrgyzstan':'Kyrgyzstan', 'Laos':'Lao PDR', 'Lebanon':'Lebanon', 'Malaysia':'Malaysia',
        'Mongolia':'Mongolia', 'Nepal':'Nepal', 'Oman':'Oman', 'Pakistan':'Pakistan',
        'Philippines':'Philippines', 'Qatar':'Qatar', 'Saudi Arabia':'Saudi Arabia',
        'Sri Lanka':'Sri Lanka', 'Syria':'Syria', 'Taiwan':'Taiwan', 'Tajikistan':'Tajikistan',
        'Thailand':'Thailand', 'Timor-Leste':'Timor-Leste', 'Turkmenistan':'Turkmenistan',
        'United Arab Emirates':'United Arab Emirates', 'Uzbekistan':'Uzbekistan',
        'Vietnam':'Vietnam', 'Yemen':'Yemen', 'Turkey':'Turkey', 'Cyprus':'Cyprus', 'Palestine':'Palestine'}

Europe = {'Russia':'Russia', 'Ukraine':'Ukraine', 'France':'France', 'Spain':'Spain', 'Sweden':'Sweden',
          'Norway':'Norway', 'Germany':'Germany', 'Finland':'Finland', 'Poland':'Poland', 'Italy':'Italy',
          'UK':'United Kingdom', 'Romania':'Romania', 'Belarus':'Belarus', 'Greece':'Greece', 'Austria':'Austria',
          'Bulgaria':'Bulgaria', 'Iceland':'Iceland', 'Hungary':'Hungary', 'Portugal':'Portugal',
          'Czech Republic':'Czech Rep.', 'Serbia':'Serbia', 'Ireland':'Ireland', 'Luxembourg':'Luxembourg',
          'Latvia':'Latvia', 'Lithuania':'Lithuania', 'Croatia':'Croatia', 'Bosnia and Herzegovina':'Bosnia and Herz.',
          'Slovakia':'Slovakia', 'Estonia':'Estonia', 'Denmark':'Denmark', 'Switzerland':'Switzerland',
          'The Netherlands':'Netherlands', 'Moldova':'Moldova', 'Belgium':'Belgium', 'Albania':'Albania',
          'Macedonia':'Macedonia', 'Slovenia':'Slovenia', 'Montenegro':'Montenegro', 'Kosovo':'Kosovo'}

North_America = {'Canada':'Canada', 'USA':'United States'}

Oceania = {'Australia':'Australia', 'Papua New Guinea':'Papua New Guinea', 'Vanuatu':'Vanuatu',
           'New Zealand':'New Zealand', 'Solomon Islands':'Solomon Is.'}

South_Central_America = {'Brazil':'Brazil', 'Colombia':'Colombia', 'Argentina':'Argentina', 'Peru':'Peru',
                         'Venezuela':'Venezuela', 'Chile':'Chile', 'Ecuador':'Ecuador', 'Bolivia':'Bolivia', 
                         'Paraguay':'Paraguay', 'Uruguay':'Uruguay', 'Guyana':'Guyana', 'Suriname':'Suriname',
                         'Mexico':'Mexico', 'Guatemala':'Guatemala', 'Cuba':'Cuba', 'Haiti':'Haiti',
                         'Dominican Republic':'Dominican Rep.', 'Honduras':'Honduras', 'El Salvador':'El Salvador',
                         'Nicaragua':'Nicaragua', 'Costa Rica':'Costa Rica', 'Panama':'Panama',  'Belize':'Belize',
                         'Jamaica':'Jamaica', 'Trinidad and Tobago':'Trinidad and Tobago', 'The Bahamas':'Bahamas'}

# Creating an inverse dictionary for fast look up later on

inv_af = {value: key for key, value in Africa.items()}
inv_as = {value: key for key, value in Asia.items()}
inv_eu = {value: key for key, value in Europe.items()}
inv_na = {value: key for key, value in North_America.items()}
inv_oc = {value: key for key, value in Oceania.items()}
inv_sa = {value: key for key, value in South_Central_America.items()}
inv_dic = {**inv_af, **inv_as, **inv_eu, **inv_na, **inv_oc, **inv_sa}
dic = {value: key for key, value in inv_dic.items()}

# Creating lists of nations categorized by the World Bank

high = ['Andorra', 'Antigua and Barbuda', 'Aruba', 'Australia', 'Austria', 'The Bahamas', 'Bahrain',
        'Barbados', 'Belgium', 'Bermuda', 'Brunei', 'Canada', 'The Cayman Islands', 'Channel Islands',
        'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Equatorial Guinea', 'Estonia', 'Faeroe Islands',
        'Finland', 'France', 'French Polynesia', 'Germany', 'Greece', 'Greenland', 'Hong Kong', 'Hungary',
        'Iceland', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Japan', 'Korea', 'Kuwait', 'Liechtenstein',
        'Luxembourg', 'Macao', 'Malta', 'Monaco', 'The Netherlands', 'New Caledonia', 'New Zealand',
        'Northern Mariana Islands', 'Norway', 'Oman', 'Portugal', 'Qatar', 'San Marino', 'Saudi Arabia',
        'Singapore', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Trinidad and Tobago',
        'United Arab Emirates', 'UK', 'USA']

upper_mid = ['Algeria', 'American Samoa', 'Argentina', 'Belarus', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
             'Bulgaria', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Fiji',
             'Gabon', 'Grenada', 'Jamaica', 'Kazakhstan', 'Latvia', 'Lebanon', 'Libya', 'Lithuania', 'Macedonia',
             'Malaysia', 'Mauritius', 'Mexico', 'Montenegro', 'Namibia', 'Palau', 'Panama', 'Peru', 'Poland',
             'Romania', 'Russia', 'Serbia', 'Seychelles', 'South Africa', 'Saint Kitts and Nevis', 'Saint Lucia',
             'Saint Vincent and the Grenadines', 'Suriname', 'Turkey', 'Uruguay', 'Venezuela']

lower_mid = ['Albania', 'Angola', 'Armenia', 'Azerbaijan', 'Belize', 'Bhutan', 'Bolivia', 'Cabo Verde', 'Cameroon',
             'China', 'Republic of the Congo', 'Ivory Coast', 'Djibouti', 'Ecuador', 'Egypt', 'El Salvador', 'Georgia',
             'Guatemala', 'Guyana', 'Honduras', 'India', 'Indonesia', 'Iran', 'Iraq', 'Jordan', 'Kiribati',
             'Kosovo', 'Lesotho', 'Maldives', 'Marshall Islands', 'Micronesia', 'Moldova', 'Mongolia', 'Morocco',
             'Nicaragua', 'Nigeria', 'Pakistan', 'Papua New Guinea', 'Paraguay', 'Philippines', 'Samoa',
             'Sao Tome and Principe', 'Solomon Islands', 'Sri Lanka', 'Sudan', 'Eswatini', 'Syria', 'Palestine',
             'Thailand', 'Timor-Leste', 'Tonga', 'Tunisia', 'Turkmenistan', 'Ukraine', 'Vanuatu', 'West Bank and Gaza']

low = ['Afghanistan', 'Bangladesh', 'Benin', 'Burkina Faso', 'Burundi', 'Cambodia', 'Central African Republic',
       'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Eritrea', 'Ethiopia', 'The Gambia', 'Ghana', 'Guinea',
       'Guinea-Bissau', 'Haiti', 'Kenya', 'Korea, Dem. Rep.', 'Kyrgyzstan', 'Laos', 'Liberia', 'Madagascar', 'Malawi',
       'Mali', 'Mauritania', 'Mozambique', 'Myanmar', 'Nepal', 'Niger', 'Rwanda', 'Senegal', 'Sierra Leone', 'Somalia',
       'Tajikistan', 'Tanzania', 'Togo', 'Uganda', 'Uzbekistan', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

# Creating a dictionary for all countries of top collaborator -- maybe just look up max val in data and find indexed col name

df2018 = [data18.columns[data18[nat].idxmax()] for nat in data18.columns]
dfall = [data.columns[data[nat].idxmax()] for nat in data.columns]

# Defining a helper function for creating lists of names that match the naturalearth_lowres data set

def helper(lis,dic,cols):
    
    lis = list(lis)
    out = []
    out2 = []

    for l in lis:
    
        try:
        
            out.append(dic[l])
            out2.append(cols[lis.index(l)])
            
        except:
        
            continue
    
    return out, out2

# Creating regional lists for map creation

AF, AF2 = helper(data.columns, Africa, dfall)
AS, AS2 = helper(data.columns, Asia, dfall)
EU, EU2 = helper(data.columns, Europe, dfall)
NA, NA2 = helper(data.columns, North_America, dfall)
OC, OC2 = helper(data.columns, Oceania, dfall)
SA, SA2 = helper(data.columns, South_Central_America, dfall)

AF18, AF182 = helper(data18.columns, Africa, df2018)
AS18, AS182 = helper(data18.columns, Asia, df2018)
EU18, EU182 = helper(data18.columns, Europe, df2018)
NA18, NA182 = helper(data18.columns, North_America, df2018)
OC18, OC182 = helper(data18.columns, Oceania, df2018)
SA18, SA182 = helper(data18.columns, South_Central_America, df2018)

# Changing continent status in world dataframe to match regions used in paper and imporve plot quality

for w in range(len(world.continent)):
    
    if world.continent[w] == 'North America':

        if world.name[w] not in ['Canada', 'United States', 'Greenland']:
            
            world.continent[w] = 'South America'

world.continent[world[world.name == 'Fiji'].index.values.astype(int)[0]] = 'Seven seas (open ocean)'
world.continent[world[world.name == 'Greenland'].index.values.astype(int)[0]] = 'Seven seas (open ocean)'

# Creating a new column to add to world for plotting most frequent collaborator nation

national = []
national18 = []

for w in world.name:
    
    try:
        
        national.append(dfall[data.columns.tolist().index(inv_dic[w])])

    except:
        
        national.append('N/A')
        
    try:

        national18.append(df2018[data18.columns.tolist().index(inv_dic[w])])
        
    except:
        
        national18.append('N/A')

# Creating a new column to add to world for plotting most frequent collaborator continent

continental = []
continental18 = []

for w in world.name:
    
    try:
        
        continental.append(world[world.name == dic[dfall[data.columns.tolist().index(inv_dic[w])]]].continent.values[0])

    except:
        
        continental.append('N/A')
        
    try:

        continental18.append(world[world.name == dic[df2018[data18.columns.tolist().index(inv_dic[w])]]].continent.values[0])
        
    except:
        
        continental18.append('N/A')

# Creating a new column to add to world for plotting most frequent collaborator income group

incgrp = []
incgrp18 = []

for n in national:
    
    if n in high:
        
        incgrp.append('High')
    
    elif n in upper_mid:
        
        incgrp.append('Upper Mid')
        
    elif n in lower_mid:
        
        incgrp.append('Lower Mid')
        
    elif n in low:
        
        incgrp.append('Low')
    
    else:
        
        incgrp.append('N/A')

for n in national18:
    
    if n in high:
        
        incgrp18.append('High')
    
    elif n in upper_mid:
        
        incgrp18.append('Upper Mid')
        
    elif n in lower_mid:
        
        incgrp18.append('Lower Mid')
        
    elif n in low:
        
        incgrp18.append('Low')
    
    else:
        
        incgrp18.append('N/A') 

# Joining dataframes

national = pd.DataFrame(national, columns = ['MFC Nation'])
national18 = pd.DataFrame(national18, columns = ['MFC Nation'])
continental = pd.DataFrame(continental, columns = ['MFC Continent'])
continental18 = pd.DataFrame(continental18, columns = ['MFC Continent'])
incgrp = pd.DataFrame(incgrp, columns = ['MFC Income Group'])
incgrp18 = pd.DataFrame(incgrp18, columns = ['MFC Income Group'])

world18 = pd.concat([world, national18, continental18, incgrp18], axis = 1)
world = pd.concat([world, national, continental, incgrp], axis = 1)

# Creating the most frequent continental collaborator maps

cm = plt.get_cmap('tab20')
color_dict = {'Africa':0, 'Asia':1, 'Europe':2, 'North America':3, 'Oceania':4, 'South America':5, 'N/A':6}
contcols = [color_dict[key] for key in world['MFC Continent']]
contcols = pd.DataFrame(contcols, columns = ['contcols'])
world = pd.concat([world, contcols], axis = 1)
contcols18 = [color_dict[key] for key in world18['MFC Continent']]
contcols18 = pd.DataFrame(contcols18, columns = ['contcols'])
world18 = pd.concat([world18, contcols18], axis = 1)

# All years

for con in ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']:
    
    w = world[world['continent'] == con].dropna()
    color_list = [cm(i/6) for i in w.contcols]
    p = w.plot(color = 'white', edgecolor = 'black')
    
    for i in range(6):
        
        w2 = w[w.contcols == i]
        p = w2.plot(color = cm(i/5), edgecolor = 'black', ax = p)
    
    if con == 'Europe':
        
        plt.axis([-30,50,30,75])
        
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    plt.savefig('C:/Users/User/Documents/Data/MDPI/' + con + 'continent_all.eps')

# 2018

for con in ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']:
    
    w = world18[world18['continent'] == con].dropna()
    color_list = [cm(i/6) for i in w.contcols]
    p = w.plot(color = 'white', edgecolor = 'black')

    for i in range(6):
        
        w2 = w[w.contcols == i]
        p = w2.plot(color = cm(i/5), edgecolor = 'black', ax = p)
    
    if con == 'Europe':
        
        plt.axis([-30,50,30,75])
        
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    plt.savefig('C:/Users/User/Documents/Data/MDPI/' + con + 'continent_2018.eps')

# Creating the most frequent income group collaborator maps

cm = plt.get_cmap('tab20b')
color_dict = {'High':0, 'Upper Mid':1, 'Lower Mid':2, 'Low':3, 'N/A':4}
inccols = [color_dict[key] for key in world['MFC Income Group']]
inccols = pd.DataFrame(inccols, columns = ['inccols'])
world = pd.concat([world, inccols], axis = 1)
inccols18 = [color_dict[key] for key in world18['MFC Income Group']]
inccols18 = pd.DataFrame(inccols18, columns = ['inccols'])
world18 = pd.concat([world18, inccols18], axis = 1)

# All years

for con in ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']:
    
    w = world[world['continent'] == con].dropna()
    color_list = [cm(i/3) for i in w.inccols]
    p = w.plot(color = 'white', edgecolor = 'black')

    for i in range(4):
        
        w2 = w[w.inccols == i]
        p = w2.plot(color = cm(i/3), edgecolor = 'black', ax = p)
    
    if con == 'Europe':
        
        plt.axis([-30,50,30,75])
        
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    plt.savefig('C:/Users/User/Documents/Data/MDPI/' + con + 'incgrp_all.eps')

# 2018

for con in ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']:
    
    w = world18[world18['continent'] == con].dropna()
    color_list = [cm(i/3) for i in w.inccols]
    p = w.plot(color = 'white', edgecolor = 'black')

    for i in range(4):
        
        w2 = w[w.inccols == i]
        p = w2.plot(color = cm(i/3), edgecolor = 'black', ax = p)
    
    if con == 'Europe':
        
        plt.axis([-30,50,30,75])
        
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    plt.savefig('C:/Users/User/Documents/Data/MDPI/' + con + 'incgrp_18.eps')

