# This script does initial data analysis for the first paper in the MDPI project

# Importing required modules

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Loading data

data_high = pd.read_csv('C:/Users/User/Documents/Data/MDPI/summary_table_high_income.csv')
data_upper_mid = pd.read_csv('C:/Users/User/Documents/Data/MDPI/summary_table_upper_mid_income.csv')
data_lower_mid = pd.read_csv('C:/Users/User/Documents/Data/MDPI/summary_table_lower_mid_income.csv')
data_low = pd.read_csv('C:/Users/User/Documents/Data/MDPI/summary_table_low_income.csv')
totals = pd.read_csv('C:/Users/User/Documents/Data/MDPI/totals_by_year_by_classification.csv')

# (1) Testing to see if the distributions by income group are pairwise similar

# (1.1) Create a function for Kolmorogorov-Smirnov Tests

def KS_test(C1,C2,a):

    D = 0
    
    for x in range(len(C1)):
        
        if abs(C1[x] - C2[x]) > D:
            
            D = abs(C1[x] - C2[x])

    val = np.sqrt(-.5 * np.log(a)) * np.sqrt((1/len(C1)) + (1/len(C1)))
    
    if D > val:
        
        out = 'The two distributions are significantly different.     -  ' + str(round(D,2)) + '  >  ' + str(round(val,2))
        
    else:
        
        out = 'The two distributions are not significantly different. -  ' + str(round(D,2)) + '  <  ' + str(round(val,2))

    return out

# (1.2) Create a function for making empirical distribution functions

def edf(C,i):
    
    edf_val = sum(C.values[0][1:i+1])
    
    return edf_val

# (1.3) For each year do the following: (years 2014-2018 chosen to ensure at least 100 low income papers per year)

for yr in range(2014,2019):

    # (1.3.1) Create CDFs for each income group
   
    temp_high = data_high[data_high['Year'] == str(yr)]
    temp_upper_mid = data_upper_mid[data_upper_mid['Year'] == str(yr)]
    temp_lower_mid = data_lower_mid[data_lower_mid['Year'] == str(yr)]
    temp_low = data_low[data_low['Year'] == str(yr)]
    
    CDF_high = [edf(temp_high,i) for i in range(1,26)] # 26 becasue the max # of collabs on any paper is 25
    CDF_upper_mid = [edf(temp_upper_mid,i) for i in range(1,26)]
    CDF_lower_mid = [edf(temp_lower_mid,i) for i in range(1,26)]
    CDF_low = [edf(temp_low,i) for i in range(1,26)]
    
    CDF_high_robust = [edf(temp_high,i) for i in range(1,21)] # 21 because this is the robustness check removing papers w/ >20 nations 
    CDF_upper_mid_robust = [edf(temp_upper_mid,i) for i in range(1,21)]
    CDF_lower_mid_robust = [edf(temp_lower_mid,i) for i in range(1,21)]
    CDF_low_robust = [edf(temp_low,i) for i in range(1,21)]
    
    # (1.3.2) Do pairwise Kolmorogorov-Smirnov tests
    
    A = [CDF_high, CDF_high, CDF_high, CDF_upper_mid, CDF_upper_mid, CDF_lower_mid]
    B = [CDF_upper_mid, CDF_lower_mid, CDF_low, CDF_lower_mid, CDF_low, CDF_low]
    
    A_robust = [CDF_high_robust, CDF_high_robust, CDF_high_robust, CDF_upper_mid_robust, CDF_upper_mid_robust, CDF_lower_mid_robust]
    B_robust = [CDF_upper_mid_robust, CDF_lower_mid_robust, CDF_low_robust, CDF_lower_mid_robust, CDF_low_robust, CDF_low_robust]

    A2 = ['CDF_high', 'CDF_high', 'CDF_high', 'CDF_upper_mid', 'CDF_upper_mid', 'CDF_lower_mid']
    B2 = ['CDF_upper_mid', 'CDF_lower_mid', 'CDF_low', 'CDF_lower_mid', 'CDF_low', 'CDF_low']
    
    for i in range(len(A)):
        
        result = KS_test(A[i],B[i],.05)
        result_robust_05 = KS_test(A_robust[i],B_robust[i],.05)
        result_robust_10 = KS_test(A_robust[i],B_robust[i],.1)
        print(result)
        
        for x in [result_robust_05,result_robust_10]:
        
            if result[0:50] == x[0:50]:
            
                continue
        
            else:
                
                print('Year == ' + str(yr) + ': ' + ['5','10'][[result_robust_05,result_robust_10].index(x)] + '% significance level')
                print(A2[i])
                print(result)
                print(B2[i])
                print(x)
                print('The results are NOT robust.')

# (1.4) Creating a heatmap of the results

M = np.zeros((4,20))
M[3,[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18]] = [1 for i in range(15)]
M[[0,1,2],3] = [1,1,1]
M[[0,1,2],7] = [1,1,1]
M[[0,1,2],11] = [1,1,1]
M[[0,1,2],15] = [1,1,1]
M[[0,1,2],19] = [1,1,1]
ylabels = ['High', 'Upper Mid', 'Lower Mid', 'Low']
xlabels = ['High', 'Upper Mid', 'Lower Mid', 'Low', 'High', 'Upper Mid', 'Lower Mid', 'Low', 'High', 'Upper Mid',
           'Lower Mid', 'Low', 'High', 'Upper Mid', 'Lower Mid', 'Low','High', 'Upper Mid', 'Lower Mid', 'Low']
fig, ax = plt.subplots(figsize = (8,5))
ax.imshow(M, cmap = 'Greys')
ax.set_xticks(np.arange(len(xlabels)))
ax.set_yticks(np.arange(len(ylabels)))
ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels)
plt.setp(ax.get_xticklabels(), rotation = 45, ha = 'right', rotation_mode = 'anchor')
fig.tight_layout()
plt.title('2014                  2015                  2016                  2017                  2018')
plt.savefig('C:/Users/User/Documents/Data/MDPI/KStest_heatmap.eps')

# (2) Population based statistics

popdata = pd.read_csv('C:/Users/User/Documents/Data/MDPI/pop_data.csv')

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

output = [0,0,0,0]

for i in range(len(popdata.Country)):
    
    if popdata.Country[i] in high:
        
        if popdata.Country[i] != 'Taiwan': # Taiwan has no data available
        
            output[0] += popdata['2018'][i]
    
    elif popdata.Country[i] in upper_mid:
    
        output[1] += popdata['2018'][i]
        
    elif popdata.Country[i] in lower_mid:
        
        output[2] += popdata['2018'][i]
        
    else: # Eritrea has data through 2011 only
        
        if popdata.Country[i] != 'Eritrea':
            
            output[3] += popdata['2018'][i]
            
        else:
            
            output[3] += popdata['2011'][i]

# The per capita results table data

output.append(sum(output))
papers = [137786,24403,54412,2573,190186]
per_cap = [papers[i]/output[i] for i in range(len(output))]

# Time series trebds for one nation only papers by income group

cm = plt.get_cmap('gist_rainbow')
xlabs = [2000 + 2*i for i in range(10)]
ylabs = [0, 20, 40, 60, 80, 100]
fig, ax = plt.subplots()
plt.plot(data_high['Year'].values[4:23], 100*data_high['1'].values[4:23], label = 'High Income', color = cm(0))
plt.plot(data_high['Year'].values[4:23], 100*data_upper_mid['1'].values[4:23], label = 'Upper Middle Income', color = cm(90))
plt.plot(data_high['Year'].values[4:23], 100*data_lower_mid['1'].values[4:23], label = 'Lower Middle Income', color = cm(180))
plt.plot(data_high['Year'].values[4:23], 100*data_low['1'].values[4:23], label = 'Low Income', color = cm(20))
plt.title('Percentage of papers with all authors from same country', loc = 'center', fontsize = 12, fontweight = 40, color = 'black')
lgd = plt.legend(loc = 'upper center', ncol = 1, bbox_to_anchor = (1.3,0.8), shadow = True)
plt.ylabel('Percentage')
plt.ylim(0,100)
plt.setp(ax.get_xticklabels(), rotation = 45, ha = 'right', rotation_mode = 'anchor')
plt.savefig('C:/Users/User/Documents/Data/MDPI/singlenat_ts_plot.eps', bbox_extra_artists = (lgd,), bbox_inches = 'tight')

