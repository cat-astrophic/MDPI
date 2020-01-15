# This script creates summary statistics and histograms for the MDPI data set

# Importing required modules

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')

# List of files to read

repetitions = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
             '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 'all']

# A function for making and saving histograms

def histogram_maker(rep, Cols, group):
    
    try:
        
        num_collabs = Cols.count(axis = 1)
        plt.hist(num_collabs, max(max(num_collabs),5), facecolor = 'red', align = 'mid', range = (0.5,max(max(num_collabs),5)+0.5))        
        plt.xticks(range(1,max(max(num_collabs)+1,6)))
        locs, labels = plt.yticks()
        plt.yticks([int(round(loc)) for loc in locs])
        plt.title('Collaboration Histogram for ' + group + ' - ' + rep + '\n')
        plt.xlabel('Number of Collaborating Nations')
        plt.ylabel('Frequency')
        
        if group == 'South/Central America':
            
            plt.savefig('C:/Users/User/Documents/Data/MDPI/histogram_South_Central_America_' + rep + '.eps', bbox_inches='tight')
        
        else:
        
            plt.savefig('C:/Users/User/Documents/Data/MDPI/histogram_' + group + '_' + rep + '.eps', bbox_inches='tight')
        
        plt.show()

    except:
        
        pass

# A function for making summary data tables

def data_table(rep, Cols, tab):
    
    num_collabs = Cols.count(axis = 1)
    row = [rep]
    
    for i in range(1,26):
        
        if len(num_collabs) > 0:
        
            row.append(len(num_collabs[num_collabs == i]) / len(num_collabs))

        else:
            
            row.append(0)
    
    row = pd.DataFrame([row], columns = tab.columns)
    tab = pd.concat([tab, row], axis = 0)
    
    return tab

# A function to subset the Collaborators DataFrame by classification

def subsetter(Collaborators, group):
    
    output = pd.DataFrame(columns = Collaborators.columns)
    
    for i in range(len(Collaborators)):
        
        for member in Collaborators.iloc[i]:
            
            if member in group:
                
                row = pd.DataFrame([Collaborators.iloc[i]], columns = Collaborators.columns)
                output = pd.concat([output, row], axis = 0)
                
                break
    
    return output

# A function to create stacked histograms by classification or region

def group_bars(data, labels, x_string, y_string, rep):
    
    plt.close()
    x_pos = [i for i, _ in enumerate(labels)]
    plt.bar(x_pos, data, color = 'green')
    plt.xlabel(x_string)
    plt.ylabel(y_string)
    plt.title('Frequency by ' + x_string + ' in ' + rep + '\n')
    plt.xticks(x_pos, labels)
    locs, labels = plt.yticks()
    plt.yticks([int(round(loc)) for loc in locs])
    plt.savefig('C:/Users/User/Documents/Data/MDPI/bar_chart_' + x_string + '_' + rep + '.eps', bbox_inches='tight')
    plt.show()

# Initializing WDI classification DataFrames

sum_tab_all = pd.DataFrame(columns = ['Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                      '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'])
sum_tab_high = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_upper_mid = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_lower_mid = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_low = pd.DataFrame(columns = sum_tab_all.columns)

# Initializing regional DataFrames

sum_tab_Africa = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_Asia = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_Europe = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_Oceania = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_North_America = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_South_Central_America = pd.DataFrame(columns = sum_tab_all.columns)

# Initializing group level summary statistics DataFrames

blank_income = np.zeros((5,25))
blank_region = np.zeros((7,25))
income_group_total_df = pd.DataFrame(blank_income, columns = ['Classification', '1996', '1997', '1998', '1999', '2000', '2001',
                                                              '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                                              '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 'all'])
income_group_percent_df = pd.DataFrame(blank_income, columns = income_group_total_df.columns)
regional_group_total_df = pd.DataFrame(blank_region, columns = ['Region', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                                                                '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                                                '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 'all'])
regional_group_percent_df = pd.DataFrame(blank_region, columns = regional_group_total_df.columns)
income_groups = ['All', 'High', 'Upper Mid', 'Lower Mid', 'Low']
regional_groups = ['All', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South and Central America']

for i in range(len(income_groups)):
    
    income_group_total_df['Classification'][i] = income_groups[i]
    
income_group_percent_df['Classification'] = income_group_total_df['Classification']

for i in range(len(regional_groups)):
    
    regional_group_total_df['Region'][i] = regional_groups[i]
    
regional_group_percent_df['Region'] = regional_group_total_df['Region']

# List for plots

regional_names_for_plots = ['All', 'Africa', 'Asia', 'Europe', 'N A', 'Oceania', 'S/C A']

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

# Creating lists of nations categorized by region

Africa = ['Nigeria', 'Ethiopia', 'Egypt', 'Democratic Republic of the Congo', 'South Africa', 'Tanzania',
          'Kenya', 'Sudan', 'Algeria', 'Uganda', 'Morocco', 'Mozambique', 'Ghana', 'Angola', 'Ivory Coast',
          'Madagascar', 'Cameroon', 'Niger', 'Burkina Faso', 'Mali', 'Malawi', 'Zambia', 'Somalia', 'Senegal',
          'Chad', 'Zimbabwe', 'Rwanda', 'Tunisia', 'Guinea', 'Benin', 'Burundi', 'South Sudan', 'Togo', 'Eritrea',
          'Sierra Leone', 'Libya', 'Republic of the Congo', 'Central African Republic', 'Liberia', 'Mauritania',
          'Namibia', 'Botswana', 'Lesotho', 'The Gambia', 'Gabon', 'Guinea-Bissau', 'Mauritius', 'Equatorial Guinea',
          'Eswatini', 'Djibouti', 'Comoros', 'Cabo Verde', 'Western Sahara', 'Sao Tome and Príncipe', 'Seychelles']

Asia = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Myanmar', 'Cambodia',
        'China', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan',
        'Kazakhstan', 'Korea, Dem. Rep.', 'Korea', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macau', 'Malaysia',
        'Maldives', 'Mongolia', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore',
        'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkmenistan',
        'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen', 'Turkey', 'Cyprus', 'Palestine']

Europe = ['Russia', 'Ukraine', 'France', 'Spain', 'Sweden', 'Norway', 'Germany', 'Finland', 'Poland', 'Italy',
          'UK', 'Romania', 'Belarus', 'Greece', 'Bulgaria', 'Iceland', 'Hungary', 'Portugal', 'Austria',
          'Czech Republic', 'Serbia', 'Ireland', 'Latvia', 'Lithuania', 'Croatia', 'Bosnia and Herzegovina',
          'Slovakia', 'Estonia', 'Denmark', 'Switzerland', 'The Netherlands', 'Moldova', 'Belgium', 'Albania',
          'Macedonia', 'Slovenia', 'Montenegro', 'Kosovo', 'Luxembourg', 'Andorra', 'Malta', 'Liechtenstein',
          'San Marino', 'Monaco', 'Vatican City']

North_America = ['Canada', 'USA']

Oceania = ['Australia', 'Papua New Guinea', 'New Zealand', 'Fiji', 'Solomon Islands', 'Vanuatu', 'Samoa',
           'Kiribati', 'Micronesia', 'Tonga', 'Marshall Islands', 'Palau', 'Tuvalu', 'Nauru']

South_Central_America = ['Brazil', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador', 'Bolivia', 
                         'Paraguay', 'Uruguay', 'Guyana', 'Suriname', 'French Guiana', 'Mexico', 'Guatemala',
                         'Cuba', 'Haiti', 'Dominican Republic', 'Honduras', 'El Salvador', 'Nicaragua',
                         'Costa Rica', 'Panama', 'Jamaica', 'Trinidad and Tobago', 'The Bahamas', 'Belize',
                         'Barbados', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Grenada',
                         'Antigua and Barbuda', 'Dominica', 'Saint Kitts and Nevis', 'The Cayman Islands']

# Main loop

for rep in repetitions:

    # Reading in the data from MDPI_interaction_matrix.py
    
    Collaborators = pd.read_csv('C:/Users/User/Documents/Data/MDPI/Collaborators_' + rep + '.csv')
    
    # Subsetting the collaboration data for developing and leas developed UN classifications

    High_Collabs = subsetter(Collaborators, high)
    Upper_Mid_Collabs = subsetter(Collaborators, upper_mid)
    Lower_Mid_Collabs = subsetter(Collaborators, lower_mid)
    Low_Collabs = subsetter(Collaborators, low)
    Africa_Collabs = subsetter(Collaborators, Africa)
    Asia_Collabs = subsetter(Collaborators, Asia)
    Europe_Collabs = subsetter(Collaborators, Europe)
    North_America_Collabs = subsetter(Collaborators, North_America)
    Oceania_Collabs = subsetter(Collaborators, Oceania)
    South_Central_America_Collabs = subsetter(Collaborators, South_Central_America)
    
    # Creating histograms of the number of unique countries represented on published papers

    histogram_maker(rep, Collaborators, 'All Nations')
    histogram_maker(rep, High_Collabs, 'High Income')
    histogram_maker(rep, Upper_Mid_Collabs, 'Upper-Middle Income')
    histogram_maker(rep, Lower_Mid_Collabs, 'Lower-Middle Income')
    histogram_maker(rep, Low_Collabs, 'Low Income')
    histogram_maker(rep, Africa_Collabs, 'Africa')
    histogram_maker(rep, Asia_Collabs, 'Asia')
    histogram_maker(rep, Europe_Collabs, 'Europe')
    histogram_maker(rep, North_America_Collabs, 'North America')
    histogram_maker(rep, Oceania_Collabs, 'Oceania')
    histogram_maker(rep, South_Central_America_Collabs, 'South/Central America')
    
    # Creating the summary data tables

    sum_tab_all = data_table(rep, Collaborators, sum_tab_all)
    sum_tab_high = data_table(rep, High_Collabs, sum_tab_high)
    sum_tab_upper_mid = data_table(rep, Upper_Mid_Collabs, sum_tab_upper_mid)
    sum_tab_lower_mid = data_table(rep, Lower_Mid_Collabs, sum_tab_lower_mid)
    sum_tab_low = data_table(rep, Low_Collabs, sum_tab_low)
    sum_tab_Africa = data_table(rep, Africa_Collabs, sum_tab_Africa)
    sum_tab_Asia = data_table(rep, Asia_Collabs, sum_tab_Asia)
    sum_tab_Europe = data_table(rep, Europe_Collabs, sum_tab_Europe)
    sum_tab_North_America = data_table(rep, North_America_Collabs, sum_tab_North_America)    
    sum_tab_Oceania = data_table(rep, Oceania_Collabs, sum_tab_Oceania)
    sum_tab_South_Central_America = data_table(rep, South_Central_America_Collabs, sum_tab_South_Central_America)
    
    # Creating per group and group level per capita summary statistics on total papers published in MDPI journals
    
    # Groups total publications and relative frequency of appearance by year

    inc_dic = {'All': len(Collaborators), 'High': len(High_Collabs), 'Upper Mid': len(Upper_Mid_Collabs),
               'Lower Mid': len(Lower_Mid_Collabs), 'Low': len(Low_Collabs)}
    reg_dic = {'All': len(Collaborators), 'Africa': len(Africa_Collabs), 'Asia': len(Asia_Collabs),
               'Europe': len(Europe_Collabs), 'North America': len(North_America_Collabs), 'Oceania': len(Oceania_Collabs),
               'South and Central America': len(South_Central_America_Collabs)}

    for group in inc_dic:
        
        income_group_total_df[rep][income_group_total_df.index[income_group_total_df['Classification'] == group].tolist()] = inc_dic[group]
        income_group_percent_df[rep][income_group_percent_df.index[income_group_percent_df['Classification'] == group].tolist()] = inc_dic[group] / inc_dic['All']
        
    for reg in reg_dic:
        
        regional_group_total_df[rep][regional_group_total_df.index[regional_group_total_df['Region'] == reg].tolist()] = reg_dic[reg]
        regional_group_percent_df[rep][regional_group_percent_df.index[regional_group_percent_df['Region'] == reg].tolist()] = reg_dic[reg] / reg_dic['All']
            
    # Do stacked histograms where totals are the same as 'all' above and stacks are either classifications or regions

    group_bars(regional_group_total_df[rep].values, regional_names_for_plots, 'Region', 'Number of Papers', rep)
    group_bars(income_group_total_df[rep].values, income_group_total_df['Classification'].values, 'Classification', 'Number of Papers', rep)
    
    # Pairwise interactions by region and classification for all years
    
    if rep == 'all':
        
        nc = Collaborators.count(axis = 1)
        rr = np.zeros((len(nc),6))
        cc = np.zeros((len(nc),4))
        R = np.zeros((6,6))
        C = np.zeros((4,4))

        for i in range(len(Collaborators)):
    
            for j in range(nc[i]):
        
                if Collaborators.iloc[i][j] in high:
            
                    cc[i][0] += 1
            
                elif Collaborators.iloc[i][j] in upper_mid:
            
                    cc[i][1] += 1
            
                elif Collaborators.iloc[i][j] in lower_mid:
            
                    cc[i][2] += 1
            
                else:
            
                    cc[i][3] += 1
    
            for j in range(nc[i]):
        
                if Collaborators.iloc[i][j] in Africa:
            
                    rr[i][0] += 1
            
                elif Collaborators.iloc[i][j] in Asia:
            
                    rr[i][1] += 1
            
                elif Collaborators.iloc[i][j] in Europe:
            
                    rr[i][2] += 1
            
                elif Collaborators.iloc[i][j] in North_America:
            
                    rr[i][3] += 1
            
                elif Collaborators.iloc[i][j] in Oceania:    
            
                    rr[i][4] += 1
            
                else:
            
                    rr[i][5] += 1
                    
        for i in range(len(nc)):
            
            for j in range(6):
                
                for k in range(j,6):
                    
                    if j == k:
                        
                        if rr[i][j] > 1:
                            
                            R[j][j] += 1
                    
                    else:
        
                        if rr[i][j] > 0 and rr[i][k] > 0:
                        
                            R[j][k] += 1
                            R[k][j] += 1
            
            for j in range(4):
        
                for k in range(j,4):
                    
                    if j == k:
                        
                        if cc[i][j] > 1:
                        
                            C[j][j] += 1
        
                    else:
                        
                        if cc[i][j] > 0 and cc[i][k] > 0:
                            
                            C[j][k] += 1
                            C[k][j] += 1
                        
        R = pd.DataFrame(R, columns = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South and Central America'])
        C = pd.DataFrame(C, columns = ['High', 'Upper Mid', 'Lower Mid', 'Low'])
        
# Write all finalized DataFrames to csv

sum_tab_all.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_all.csv', index = False)
sum_tab_high.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_high_income.csv', index = False)
sum_tab_upper_mid.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_upper_mid_income.csv', index = False)
sum_tab_lower_mid.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_lower_mid_income.csv', index = False)
sum_tab_low.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_low_income.csv', index = False)
sum_tab_Africa.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_Africa.csv', index = False)
sum_tab_Asia.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_Asia.csv', index = False)
sum_tab_Europe.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_Europe.csv', index = False)
sum_tab_Oceania.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_Oceania.csv', index = False)
sum_tab_North_America.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_North_America.csv', index = False)
sum_tab_South_Central_America.to_csv('C:/Users/User/Documents/Data/MDPI/summary_table_South_Central_America.csv', index = False)
income_group_total_df.to_csv('C:/Users/User/Documents/Data/MDPI/totals_by_year_by_classification.csv', index = False)
income_group_percent_df.to_csv('C:/Users/User/Documents/Data/MDPI/percentages_by_year_by_classification.csv', index = False)
regional_group_total_df.to_csv('C:/Users/User/Documents/Data/MDPI/totals_by_year_by_region.csv', index = False)
regional_group_percent_df.to_csv('C:/Users/User/Documents/Data/MDPI/percentages_by_year_by_region.csv', index = False)
R.to_csv('C:/Users/User/Documents/Data/MDPI/pairwise_by_region.csv', index = False)
C.to_csv('C:/Users/User/Documents/Data/MDPI/pairwise_by_classification.csv', index = False)
