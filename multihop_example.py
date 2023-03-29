# %%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seymour_creds import url, name, password, token
import pymaid
rm = pymaid.CatmaidInstance(url, token, name, password)

from contools import Promat
from data_settings import data_date_A1_brain, pairs_path

pairs = Promat.get_pairs(pairs_path=pairs_path) #csv of neuron pairs
#pairs = Promat.get_pairs(pairs_path=pairs_path, flip_weirdos=False) 
# usually this function flips the left and right IDs of neurons that have their soma in one
# brain hemisphere and their neurites in the order. You can deactivate this behaviour with flip_weirdos=False

# %%
# when looking at multihop connectivity with a threshold using individual neuron edge list (not the paired list); TESTED AND WORKING

neurons = pymaid.get_skids_by_annotation('nr test 5_1099-neuron 65408/65845') # Tel-like 10

# use pregenerated edge list
edges = Promat.pull_edges(type_edges='ad', threshold=0.01, data_date=data_date_A1_brain, pairs_combined=False)
pairs = Promat.get_pairs(pairs_path=pairs_path) #csv of neuron pairs

# downstream x-hops of Tel-like 10
downstream = Promat.downstream_multihop(edges=edges, sources=neurons, hops=2, pairs_combined=False, pairs=pairs)

# %%
# when looking at multihop connectivity with a threshold using paired-neuron edge list; TESTED AND WORKING 
# (not individual neurons; note that pair_ID refers to the left skid of a pair)

neurons = pymaid.get_skids_by_annotation('nr Tel-like 10') # Tel-like 10

# use pregenerated edge list
edges = Promat.pull_edges(type_edges='ad', threshold=0.01, data_date=data_date_A1_brain, pairs_combined=True)

# downstream 3-hops of Tel-like 10
downstream = Promat.downstream_multihop(edges=edges, sources=neurons, hops=2, pairs_combined=True)
# %%
