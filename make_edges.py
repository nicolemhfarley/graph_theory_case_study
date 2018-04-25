# Import libraries
import pandas as pd
import networkx as nx
from networkx.algorithms import community
import numpy as np
import random

# Load csv file to pandas dataframe: df
df = pd.read_csv('filtered_doctors.csv')
print('Data Loaded')

# Find all unique doctor ids: id_list
id_list = df['id'].unique()

# Create an empty dictionary 'code_dict'. Fill with {id: procedure_codes}
code_dict = dict()
for i in id_list:
    code_dict[i] =  df[df['id'] == i]['procedure_code'].values.tolist()

print('Finding all edges...')
edge_list = [] # Create an empty list to hold edges: edge_list

# Loop through each id and code values:
for k,v in code_dict.items(): # For each key, value pair
    for k2,v2 in code_dict.items(): # and for all other key, value pairs
        for c in v: # check the first code in v
            for c2 in v2: # and compare it to all the other codes in all other values
                if c == c2 and k != k2: # if the codes match and its not the same id
                    edge = (k, k2) # create an edge
                    edge_list.append(edge) # add edge to edge_list

# Remove duplicates: edge_set
edge_set = list(set(edge_list))
print('Edge list created')

# Choose a random sample of 1000 doctors: edge_set_small
random.shuffle(edge_set)
edge_set_small = edge_set[0:1000]

# Create an empty network: G
G = nx.Graph()
print('Graph created')

# Add all edges from edge_set to graph 'G'
for e in edge_set_small:
    G.add_edge(*e)

# Save 'G' to .gexf file: 'edge_list.gexf'
nx.write_gexf(G, 'edge_list_small.gexf')
community_graph = community.girvan_newman(G)
nx.write_gexf(community_graph, 'community_graphs.gexf')
print("File 'edge_list_small.gexf' created and saved to directory")
print('Done')
