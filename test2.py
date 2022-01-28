# %%
from naomi_creds import url, name, password, token
import pymaid
import numpy as np

rm = pymaid.CatmaidInstance(server=url, api_token=token, http_user=name, http_password=password, project_id=11)

# %%

# load skids for particular annotation
neurons = pymaid.get_skids_by_annotation('eyespot')

# finding upstream partners (with no threshold)
us_neurons = pymaid.get_partners(neurons, directions=['incoming']) # could add threshold here
us_2hop_neurons = pymaid.get_partners(us_neurons.skeleton_id, directions=['incoming'])

# check names
pymaid.get_names(neurons)