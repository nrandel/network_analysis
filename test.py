# %%
from seymour_creds import url, name, password, token
import pymaid
import numpy as np
import pandas as pd

rm = pymaid.CatmaidInstance(server=url, api_token=token, http_user=name, http_password=password)


# %%

# OLD
# load skids for particular annotation
neurons = pymaid.get_skids_by_annotation('nr Tel-like 10')

# finding upstream partners (with no threshold)
us_neurons = pymaid.get_partners(neurons, directions=['incoming']) # could add threshold here
us_2hop_neurons = pymaid.get_partners(us_neurons.skeleton_id, directions=['incoming'])

# skids are str by default, converted to integer
us_neurons_skids = [int(x) for x in us_neurons.skeleton_id]
us_2hop_skids = [int(x) for x in us_2hop_neurons.skeleton_id]

# identify all brain neurons in these groups
brain_neurons = pymaid.get_skids_by_annotation('mw brain neurons')
us_brain_neurons = np.intersect1d(us_neurons_skids, brain_neurons)
us_2hop_brain_neurons = np.intersect1d(us_2hop_skids, brain_neurons)

# could also filter based on number of nodes
bool_array = us_neurons.num_nodes>500
us_neurons_filtered = us_neurons[bool_array]

bool_array = us_2hop_neurons.num_nodes>500
us_2hop_neurons_filtered = us_2hop_neurons[bool_array]

# could also filter by skeleton ID; kind of silly example
bool_array = us_2hop_neurons.skeleton_id=='17378483'
us_particular_neuron = us_2hop_neurons[bool_array]

# %%
# USE CODE BELOW TO IDENTIFY WHICH NEURONS FROM CATMAID (e.g. 1 hop upstream of Tele-like 10) == activation screen
# example: compare two lists and get match
a = [1, 2, 3, 5, 4, 22]
b = [9, 8, 7, 6, 5, 22]
m = set(a) & set(b)

# %%
# open left skeleton ID of identified split-neurons from CATMAID: /Users/nadine/Documents/paper/single-larva/Left-skids_NBLAST_CleanBrain.csv
with open("/Users/nadine/Documents/paper/single-larva/generated-data/neuron-skids_nr1099uniqueIDneuron.csv", 'r') as f:
    ids_of_interest = []
    _ = f.readline() # skip first line
    for line in f:
        id = line.rstrip()
        ids_of_interest.append(id)
#print(ids_of_interest)     
#    
# %%
''''
# open skeleton ID of nr 1099 unique neurons/1hop from CATMAID "skeleton_id"
with open("/Users/nadine/Documents/paper/single-larva/skeleton_ID_nr1099-unique.csv", 'r') as f:
    ids_of_interest = []
    _ = f.readline() # skip first line
    for line in f:
        id = line.rstrip()
        ids_of_interest.append(id)
print(ids_of_interest)   
'''
# %%
#e.g., /Users/nadine/Documents/paper/single-larva/generated-data/1-hop_downstream_potential_nr-test23_1099-neuron48991_b.csv
with open("/Users/nadine/Documents/paper/single-larva/generated-data/connectivity/2-hop_downstream_nr_59a.csv", 'r') as f:
    catmaid_neurons = []
    for line in f:
        #print(line.rstrip())
        id, _ = line.rstrip().lstrip().split(',') #remove spaces and new lines on left and right side, and splitting (split returns list of strings) on the comma. '_' we ignore this variable 
        
        catmaid_neurons.append(id)
print(catmaid_neurons)    

# %%
# compare two lists. output matched values

matched = set(catmaid_neurons) & set(ids_of_interest)

print(matched)
# %%
#??
with open("/Users/nadine/Documents/paper/single-larva/generated-data/pre-post_lines.csv", 'r') as f:
    spliline_neurons = []
    for line in f:
        #print(line.rstrip())
        id = line.rstrip().lstrip() #remove spaces and new lines on left and right side 
        
        spliline_neurons.append(id)
#print(spliline_neurons)

# output: remove duplicates in list
unique = list(set(spliline_neurons))
# %%

10100020 in upstream[0]
