# %%
from naomi_creds import url, name, password, token
import pymaid
import numpy as np
import pandas as pd

import contools

rm = pymaid.CatmaidInstance(server=url, api_token=token, http_user=name, http_password=password, project_id=11)

# %%

# load skids for particular annotation
neurons = pymaid.get_skids_by_annotation('eyespot')

# finding upstream partners (with no threshold)
us_neurons = pymaid.get_partners(neurons, directions=['incoming']) # could add threshold here
us_2hop_neurons = pymaid.get_partners(us_neurons.skeleton_id, directions=['incoming'])

# check names
pymaid.get_names(neurons)

# get treenode table for skid from previously loaded neurons 
tn_table = pymaid.get_node_table(neurons[0])
tn_table.head()

# fetching neurons
n_list1 = pymaid.get_neuron(['annotation:eyespot']) #by annotation

n_list2 = pymaid.get_neuron(['772993', '57341']) #by name or skid


# %%
# finding downstream partners (with no threshold)
ds_neurons = pymaid.get_partners(neurons, directions=['outgoing']) # could add threshold here
ds_2hop_neurons = pymaid.get_partners(ds_neurons.skeleton_id, directions=['outgoing'])

# %%
# cascade using CATMAID (can be done with csv as well) https://github.com/mwinding/connectome_tools/blob/main/examples/cascade_example.ipynb

name = 'XXX cascade' 
source_skids = pymaid.get_skids_by_annotation('celltype1') 
stop_skids = pymaid.get_skids_by_annotation('motorneuron')
adj = pd.read_csv('data/adj/naomi_celltype_all-to-all.csv', index_col = 0)
adj.columns = [int(x[2:-1]) for x in adj.columns]
p = 0.15 # originally 0.05 in Drosophila dataset
max_hops = 10
n_init = 100
simultaneous = True

# %%
cascade = contools.Cascade_Analyzer.run_single_cascade(
    name = name,
    source_skids = source_skids,
    stop_skids = stop_skids,
    adj = adj,
    p = p,
    max_hops = max_hops,
    n_init = n_init,
    simultaneous = simultaneous
)
# %%
data = cascade.skid_hit_hist
data_sorted = data.sort_values(by = list(data.columns), ascending=False)
data_sorted
# %%
import seaborn as sns

sns.heatmap(data_sorted)
# %%
# find the neurons downstream of cascade

processed_data = data.drop(columns=[0])
boolean = processed_data.sum(axis=1)>=n_init/2 # all neurons with >=50 visits across all hops
skids_ds = list(processed_data.index[boolean])

# %%
# who are the neurons

pymaid.get_names(skids_ds)

# %%
