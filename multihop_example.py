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
# downstream
# when looking at multihop connectivity with a threshold using individual neuron edge list (not the paired list); TESTED AND WORKING

neurons = pymaid.get_skids_by_annotation('nr TC') # Tel-like 10, nr FW: forward triggering cells; nr TC: turn triggereing cells

# use pregenerated edge list
edges = Promat.pull_edges(type_edges='ad', threshold=0.01, data_date=data_date_A1_brain, pairs_combined=False)
pairs = Promat.get_pairs(pairs_path=pairs_path) #csv of neuron pairs

# downstream x-hops of Tel-like 10
downstream = Promat.downstream_multihop(edges=edges, sources=neurons, hops=3, pairs_combined=False, pairs=pairs)

# %%
# downstream
# when looking at multihop connectivity with a threshold using paired-neuron edge list; TESTED AND WORKING 
# (not individual neurons; note that pair_ID refers to the left skid of a pair)

neurons = pymaid.get_skids_by_annotation('nr Tel-like 10') # Tel-like 10

# use pregenerated edge list
edges = Promat.pull_edges(type_edges='ad', threshold=0.01, data_date=data_date_A1_brain, pairs_combined=True)

# downstream 3-hops of Tel-like 10
downstream = Promat.downstream_multihop(edges=edges, sources=neurons, hops=2, pairs_combined=True)
# %%
# upstream
# when looking at multihop connectivity with a threshold using individual neuron edge list (not the paired list); TESTED AND WORKING

neurons = pymaid.get_skids_by_annotation('nr test3/13_1099-neuron 11729/24010') # Tel-like 10

# use pregenerated edge list
edges = Promat.pull_edges(type_edges='ad', threshold=0.01, data_date=data_date_A1_brain, pairs_combined=False)
pairs = Promat.get_pairs(pairs_path=pairs_path) #csv of neuron pairs

# upstream x-hops of Tel-like 10
upstream = Promat.upstream_multihop(edges=edges, sources=neurons, hops=2, pairs_combined=False, pairs=pairs)

# %%
#TEST add annotations to a list of skids (missing permission for now)

pymaid.add_annotations([6572414, 5747036], ['nr test for adding annotations'])
# %%
#save output to csv
# output is list of lists and therefore the range need to be chosen. E.g., For 3-hop = upstream[2]

import csv

# Define data
data = pd.DataFrame(upstream[2])

data.to_csv('/Users/nadine/Documents/paper/single-larva/generated-data/2-hop.csv', index=False)

# %%
#Concatenate df NOT WORKING (wrong output)

data1 = pd.DataFrame(upstream)
df = [data1[0], data1[1]]
df2 = pd.concat(df)
df2.to_csv('/Users/nadine/Documents/paper/single-larva/generated-data/1_to_2-hop.csv', index=False)

# %%
# %%

# Intersection of upstream and downstream multihop connection using annotoations
# If multihop path between source (e.g., 'FW-R1') and target (e.g., 'nr test 6_1099-neuron 62653/70584') for n hops: source 1-TO-n-1 hops downstream (path)/ source & target n hops (True/False),
# and target 1-TO-n hops upstream

# load skids for particular annotation
source = pymaid.get_skids_by_annotation('nr TC AF12_Ex2') #FW: forward triggering cells; TC: turn triggereing cells
target = pymaid.get_skids_by_annotation('nr test3/13_1099-neuron 11729/24010 3-hop upstream')

# identify multihop-path (mhp) between neuron source and target (~graph widget)
mhp = np.intersect1d(source, target)

# convert to panda and save as csv
# Define data
#data = pd.DataFrame(mhp)

#data.to_csv('/Users/nadine/Documents/paper/single-larva/generated-data/intersection_source-target.csv', index=False)

# %%
#intersect FW1-3hops and TC 1-3hops! (TODO)

# load skids for particular annotation
group1 = pymaid.get_skids_by_annotation('nr 1-TO-3_hops_downstream_nr-FW') 
group2 = pymaid.get_skids_by_annotation('nr 1-TO-3_hops_downstream_nr-TC')

# identify intersection between two groups of neuronns
gi = np.intersect1d(group1, group2)
# %%
