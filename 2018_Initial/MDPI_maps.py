# This script generates maps for collaborations during the entire time period

# Importing required modules

import numpy as np
import pandas as pd
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
cm = plt.get_cmap('tab20')

# Reading in the data

cnodes = pd.read_csv('C:/Users/User/Documents/Data/MDPI/totals_by_year_by_classification.csv')
rnodes = pd.read_csv('C:/Users/User/Documents/Data/MDPI/totals_by_year_by_region.csv')
cnodes = cnodes.iloc[1:]
rnodes = rnodes.iloc[1:]
cdata = pd.read_csv('C:/Users/User/Documents/Data/MDPI/pairwise_by_classification.csv')
rdata = pd.read_csv('C:/Users/User/Documents/Data/MDPI/pairwise_by_region.csv')

# Create a weighted copy of $K_{4}$ to illustrate classification collaboration

plt.figure(figsize = (8,8))
cwidths = [cdata.values[i][j] for i in range(4) for j in range(i,4)]
cwidths = [35 * width / max(cwidths) for width in cwidths]
cg = nx.MultiGraph([(i,j) for i in range(4) for j in range(i,4)])
clabels = {0: 'High', 1: 'Upper Mid', 2: 'Lower Mid', 3: 'Low'}
cpos = [[0,1], [1,0], [-1,0], [0,-1]]
clabpos = [[0.25,1], [1,0.25], [-1,0.25], [0.25,-1]]
nx.draw(cg, cpos, node_size = 5000 * cnodes['all'] / max(cnodes['all']), width = cwidths)
nx.draw_networkx_labels(cg, clabpos, clabels)
plt.title('Trans-Income Classification Collaborations', loc = 'center', fontsize = 24, color = 'black')
plt.savefig('C:/Users/User/Documents/Data/MDPI/graph_classifications.eps')
plt.show()

# Create a weighted copy of $K_{6}$ to illustrate classification collaboration

plt.figure(figsize = (8,8))
rwidths = [rdata.values[i][j] for i in range(6) for j in range(i,6)]
rwidths = [35 * width / max(rwidths) for width in rwidths]
rg = nx.MultiGraph([(i,j) for i in range(6) for j in range(i,6)])
rlabels = {0: 'Asia', 1: 'Oceania', 2: 'S/C America', 3: 'Europe', 4: 'Africa', 5: 'North America'}
rpos = [[0,-1], [np.sqrt(3)/2,1/2], [0,1], [-1*np.sqrt(3)/2,1/2], [np.sqrt(3)/2,-1/2], [-1*np.sqrt(3)/2,-1/2]]
rlabpos = [[np.sqrt(3)/2,3/4], [np.sqrt(3)/2,-3/4], [-1*np.sqrt(3)/2,-3/4], [0.25,1.05], [0.25,-1], [-1*np.sqrt(2.8)/2,3/4]]
nx.draw(rg, rpos, node_size = 5000 * rnodes['all'] / max(rnodes['all']), width = rwidths)
nx.draw_networkx_labels(rg, rlabpos, rlabels)
plt.title('Transcontinental Collaborations', loc = 'center', fontsize = 24, color = 'black')
plt.savefig('C:/Users/User/Documents/Data/MDPI/graph_regions.eps')
plt.show()

# Overlay the previous graph on a map of the world

plt.figure()
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est > 0) & (world.name != 'Antarctica')]
base = world.plot(color = 'white', edgecolor = 'black')
rwidths = [rdata.values[i][j] for i in range(6) for j in range(i,6)]
rwidths = [15 * width / max(rwidths) for width in rwidths]
rg = nx.MultiGraph([(i,j) for i in range(6) for j in range(i,6)])
rpos = [[25,-10], [100,40], [15,65], [-100,40], [135,-24], [-55,-20]]
nx.draw(rg, rpos, node_size = 1000 * rnodes['all'] / max(rnodes['all']), width = rwidths, node_color = cm(2/3))
plt.title('Transcontinental Collaborations', loc = 'center', fontsize = 20, color = 'black')
plt.savefig('C:/Users/User/Documents/Data/MDPI/map_regions.eps')
plt.show()

