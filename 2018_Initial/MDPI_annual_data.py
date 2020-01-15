# This script creates files containing annual MDPI data

# Importing required modules

import pandas as pd

# Reading in the input file

data = pd.read_csv('C:/Users/User/Documents/Data/MDPI/MDPIpapers_all.csv')

# Standardize year format

for i in range(len(data.Year)):
    
    if data.Year[i] < 20:
        
        data.Year[i] = data.Year[i] + 2000
    
    elif (data.Year[i] > 90) and (data.Year[i] < 100):
        
        data.Year[i] = data.Year[i] + 1900

# Create a file for each year between 1996 and 2018

for yr in range(1996,2019):
    
    sub_df = data[data.Year == yr]
    sub_df.to_csv('C:/Users/User/Documents/Data/MDPI/MDPIpapers_' + str(yr) + '.csv', index = False)

