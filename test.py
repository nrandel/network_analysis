# %%
from seymour_creds import url, name, password, token
import pymaid
import numpy as np

rm = pymaid.CatmaidInstance(server=url, api_token=token, http_user=name, http_password=password)


# %%

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