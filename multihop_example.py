# %%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seymour_creds import url, name, password, token
import pymaid
rm = pymaid.CatmaidInstance(url, token, name, password)

from contools import Promat

# %%
neurons = pymaid.get_skids_by_annotation('nr Tel-like 10') # Tel-like 10

# use pregenerated edge list
edges = pd.read_csv('data/edges_threshold/ad_pairwise-input-threshold-0.01_paired-edges_2022-11-03.csv', index_col=0)

# downstream 3-hops of Tel-like 10
downstream = Promat.downstream_multihop(edges=edges, sources=neurons, hops=1, pairs_combined=True)
# %%
