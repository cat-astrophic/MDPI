# This script creates summary statistics and histograms for the MDPI data set

# Importing required modules

import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')

# List of files to read

repetitions = ['all_cat_1', 'all_cat_2', 'all_cat_3', 'all_cat_4', 'all_cat_5', 'all_cat_6']

# A function for making and saving histograms

def histogram_maker(rep, Cols, group):
    
    try:
        
        num_collabs = Cols.count(axis = 1)
        plt.hist(num_collabs, max(max(num_collabs),5), facecolor = 'red', align = 'mid', range = (0.5,max(max(num_collabs),5)+0.5))        
        plt.xticks(range(1,max(max(num_collabs)+1,6)))
        locs, labels = plt.yticks()
        plt.yticks([int(round(loc)) for loc in locs])
        plt.title('Collaboration Histogram for ' + group + ' - ' + str(rep[-1]) + '\n')
        plt.xlabel('Number of Collaborating Nations')
        plt.ylabel('Frequency')
        plt.savefig('C:/Users/User/Documents/Data/MDPI/FM_histogram_' + group + '_' + rep + '.eps', bbox_inches = 'tight')        
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

# Initializing WDI classification DataFrames

sum_tab_all = pd.DataFrame(columns = ['Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                      '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'])
sum_tab_high = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_upper_mid = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_lower_mid = pd.DataFrame(columns = sum_tab_all.columns)
sum_tab_low = pd.DataFrame(columns = sum_tab_all.columns)

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

# Main loop

for rep in repetitions:

    # Reading in the data from MDPI_interaction_matrix.py
    
    Collaborators = pd.read_csv('C:/Users/User/Documents/Data/MDPI/FM_Collaborators_' + rep + '.csv')
    
    # Subsetting the collaboration data for UN classifications for income and region

    High_Collabs = subsetter(Collaborators, high)
    Upper_Mid_Collabs = subsetter(Collaborators, upper_mid)
    Lower_Mid_Collabs = subsetter(Collaborators, lower_mid)
    Low_Collabs = subsetter(Collaborators, low)
    
    # Creating histograms of the number of unique countries represented on published papers

    histogram_maker(rep, Collaborators, 'All Nations')
    histogram_maker(rep, High_Collabs, 'High Income')
    histogram_maker(rep, Upper_Mid_Collabs, 'Upper-Middle Income')
    histogram_maker(rep, Lower_Mid_Collabs, 'Lower-Middle Income')
    histogram_maker(rep, Low_Collabs, 'Low Income')
    
    # Creating the summary data tables

    sum_tab_all = data_table(rep, Collaborators, sum_tab_all)
    sum_tab_high = data_table(rep, High_Collabs, sum_tab_high)
    sum_tab_upper_mid = data_table(rep, Upper_Mid_Collabs, sum_tab_upper_mid)
    sum_tab_lower_mid = data_table(rep, Lower_Mid_Collabs, sum_tab_lower_mid)
    sum_tab_low = data_table(rep, Low_Collabs, sum_tab_low)
        
# Write all finalized DataFrames to csv

sum_tab_all.to_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_all.csv', index = False)
sum_tab_high.to_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_high_income.csv', index = False)
sum_tab_upper_mid.to_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_upper_mid_income.csv', index = False)
sum_tab_lower_mid.to_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_lower_mid_income.csv', index = False)
sum_tab_low.to_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_low_income.csv', index = False)

