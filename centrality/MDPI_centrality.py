# This script performs the centrality analyses for the publication network centrality project

# Import required modules

import numpy as np
import pandas as pd
import networkx as nx

# Creating a list of all countries

countries = pd.read_csv('C:/Users/User/Documents/Data/MDPI/M_all.csv').columns

# Initializing lists for eventual results dataframes

degree = []
closeness = []
betweenness = []
harmonic = []
eigenvector = []

# Run analyses for each year from 2010 through 2019 as well as for all years

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 'all']

for yr in years:
    
    # Read in the data
    
    M = pd.read_csv('C:/Users/User/Documents/Data/MDPI/M_' + yr + '.csv')

    # Compute the various centralities for all nations and store the results using networkx
    
    G = nx.Graph(M.values)
    
    dc = list(nx.algorithms.centrality.degree_centrality(G).values())
    cc = list(nx.algorithms.centrality.closeness_centrality(G).values())
    bc = list(nx.algorithms.centrality.betweenness_centrality(G).values())
    hc = list(nx.algorithms.centrality.harmonic_centrality(G).values())
    ec = list(nx.algorithms.centrality.eigenvector_centrality(G).values())
    
    # Assign empty values for nations which did not contribute to publication in that year
    
    nations = M.columns
    idset = [list(countries).index(country) for country in countries if country not in nations]
    
    # Fill in the lists of centrality values with empty values for missing indices
    
    for idx in idset:
        
        dc.insert(idx, '---')
        cc.insert(idx, '---')
        bc.insert(idx, '---')
        hc.insert(idx, '---')
        ec.insert(idx, '---')
    
    # Store these results

    degree.append(dc)
    closeness.append(cc)
    betweenness.append(bc)
    harmonic.append(hc)
    eigenvector.append(ec)
    
# Create a dataframe of the collective results for each centrality measure and save the results

years[len(years)-1] = 'All'

dcdf = pd.DataFrame(np.transpose(degree), columns = years)
ccdf = pd.DataFrame(np.transpose(closeness), columns = years)
bcdf = pd.DataFrame(np.transpose(betweenness), columns = years)
hcdf = pd.DataFrame(np.transpose(harmonic), columns = years)
ecdf = pd.DataFrame(np.transpose(eigenvector), columns = years)

dcdf.set_index(countries).to_csv('C:/Users/User/Documents/Data/MDPI/Centrality/Degree_Centrality.csv')
ccdf.set_index(countries).to_csv('C:/Users/User/Documents/Data/MDPI/Centrality/Closeness_Centrality.csv')
bcdf.set_index(countries).to_csv('C:/Users/User/Documents/Data/MDPI/Centrality/Betweenness_Centrality.csv')
hcdf.set_index(countries).to_csv('C:/Users/User/Documents/Data/MDPI/Centrality/Harmonic_Centrality.csv')
ecdf.set_index(countries).to_csv('C:/Users/User/Documents/Data/MDPI/Centrality/Eigenvector_Centrality.csv')




"""Right now this does the 5 centrality analyses"""

"""Next add the regressiona analyses and core-periphery analyses"""




# Create a network visualization and save to file

islands = [idx for idx in range(len(M)) if sum(M.values[idx]) == 0]

for island in islands:
    
    N = M.drop(M.columns[island], axis = 1).drop(island, axis = 0).values    
    
    for row in range(len(N)):
        
        for col in range(len(N)):
            
            if int(N[row,col]) > 0:
                
                N[row,col] = 1
            
    H = nx.Graph(N)

nx.draw_spring(H, node_size = 10, edge_size = 1)

