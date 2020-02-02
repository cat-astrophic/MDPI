# This script does initial data analysis on Frascati Manual categorized data for the first paper in the MDPI project 

# Importing required modules

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Loading data

data_high = pd.read_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_high_income.csv')
data_upper_mid = pd.read_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_upper_mid_income.csv')
data_lower_mid = pd.read_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_lower_mid_income.csv')
data_low = pd.read_csv('C:/Users/User/Documents/Data/MDPI/FM_summary_table_low_income.csv')

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

def edf(C,i,j):
    
    edf_val = sum(C.values[j][1:i+1])
    
    return edf_val

# (1.3) Perform the tests using the functions
    
for j in range(len(data_high)):
    
    # (1.3.1) Create CDFs for each income group
    
    CDF_high = [edf(data_high,i,j) for i in range(1,26)] # 26 becasue the max # of collabs on any paper is 25
    CDF_upper_mid = [edf(data_upper_mid,i,j) for i in range(1,26)]
    CDF_lower_mid = [edf(data_lower_mid,i,j) for i in range(1,26)]
    CDF_low = [edf(data_low,i,j) for i in range(1,26)]
    
    CDF_high_robust = [edf(data_high,i,j) for i in range(1,21)] # 21 because this is the robustness check removing papers w/ >20 nations 
    CDF_upper_mid_robust = [edf(data_upper_mid,i,j) for i in range(1,21)]
    CDF_lower_mid_robust = [edf(data_lower_mid,i,j) for i in range(1,21)]
    CDF_low_robust = [edf(data_low,i,j) for i in range(1,21)]
    
    # (1.3.2) Do pairwise Kolmorogorov-Smirnov tests
    
    A = [CDF_high, CDF_high, CDF_high, CDF_upper_mid, CDF_upper_mid, CDF_lower_mid]
    B = [CDF_upper_mid, CDF_lower_mid, CDF_low, CDF_lower_mid, CDF_low, CDF_low]
    
    A_robust = [CDF_high_robust, CDF_high_robust, CDF_high_robust, CDF_upper_mid_robust, CDF_upper_mid_robust, CDF_lower_mid_robust]
    B_robust = [CDF_upper_mid_robust, CDF_lower_mid_robust, CDF_low_robust, CDF_lower_mid_robust, CDF_low_robust, CDF_low_robust]
    
    A2 = ['CDF_high', 'CDF_high', 'CDF_high', 'CDF_upper_mid', 'CDF_upper_mid', 'CDF_lower_mid']
    B2 = ['CDF_upper_mid', 'CDF_lower_mid', 'CDF_low', 'CDF_lower_mid', 'CDF_low', 'CDF_low']
    
    for i in range(len(A)):
        
        print('\n' + data_high['Category'][j] + ' --- ' + A2[i] + ' --- ' + B2[i] + '\n')
        result = KS_test(A[i],B[i],.05)
        result_robust_05 = KS_test(A_robust[i],B_robust[i],.05)
        result_robust_10 = KS_test(A_robust[i],B_robust[i],.1)
        print(result)
        print(result_robust_05)
        print(result_robust_10)

# (1.4) Creating a heatmap of the results

M = np.zeros((8,12))
M[3,[0,1,2,4,5,6,8,9,10]] = [1 for i in range(9)]
M[7,[0,4,5,6,8]] = [1 for i in range(5)]
M[[0,1,2,4],3] = [1,1,1,1]
M[[0,1,2,4,5,6],7] = [1,1,1,1,1,1]
M[[0,1,2,4],11] = [1,1,1,1]
xlabels = ['High', 'Upper Mid', 'Lower Mid', 'Low', 'High', 'Upper Mid', 'Lower Mid', 'Low', 'High', 'Upper Mid', 'Lower Mid', 'Low']
ylabels = ['High', 'Upper Mid', 'Lower Mid', 'Low', 'High', 'Upper Mid', 'Lower Mid', 'Low']
fig, ax = plt.subplots(figsize = (6.5,4))
ax = sns.heatmap(M, cmap = 'Greys', cbar = False)
ax.set_xticks(np.arange(len(xlabels))+.5)
ax.set_yticks(np.arange(len(ylabels))+.5)
ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels)
ax.set_ylim(len(ylabels),0)
plt.setp(ax.get_xticklabels(), rotation = -45, ha = 'left', rotation_mode = 'anchor')
plt.setp(ax.get_yticklabels(), rotation = 0, ha = 'right', rotation_mode = 'anchor')
fig.tight_layout()
plt.savefig('C:/Users/User/Documents/Data/MDPI/FM_KStest_heatmap.eps')

