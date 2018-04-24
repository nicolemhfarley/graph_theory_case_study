# Import libraries
import pandas as import pd
import networkx as nx
import numpy as np

# Load csv file to pandas dataframe: df
df = pd.read_csv('filter_doctors.csv')
print('Data Loaded')

# Find all unique doctor ids: id_list
id_list = df['id'].unique()

# Create an empty dictionary and add all procedure codes for each id: code_dict
code_dict = dict()
for i in id_list:
    test_dict[i] =  df_cleaned[df_cleaned['id'] == i]['procedure_code'].values.tolist()

print('Finding all edges...')
# Loop through each id and code values:
edge_list = []
for k,v in code_dict.items(): # For each key, value pair
    for k2,v2 in code_dict.items(): # and for all other key, value pairs
        for c in v: # check the first code in v
            for c2 in v2: # and compare it to all the other codes in all other values
                if c == c2 and k != k2: # if the codes match and its not the same id
                    edge = (k, k2) # create an edge
                    edge_list.append(edge)

# Remove duplicates: edge_set
edge_set = set(edge_list)
print('Edge list created')

# Choose a random sample of 1000 doctors: edge_set_small
edge_set_small = np.random.choice(edge_set, size=1000)

# Create an empty network: G
G = nx.Graph()
print('Graph created')

# Add all edges from edge_set to graph 'G'
for e in edge_set_small:
    G.add_edge(*e)

# Save 'G' to .gexf file: 'edge_list.gexf'
nx.write_gexf(G, 'edge_list_small.gexf')
print("File 'edge_list_small.gexf' created and saved to directory")
print('Done')
