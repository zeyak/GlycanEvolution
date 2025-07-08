import pandas as pd
from glycowork.glycan_data.loader import df_glycan, df_species
from glycowork.motif.processing import presence_to_matrix
from glycowork.motif.analysis import get_heatmap
from glycowork.motif.analysis import plot_embeddings

df_fish = df_species[df_species.Class == 'Actinopterygii'].reset_index(drop = True)
df_map_fish = presence_to_matrix(df_fish, label_col_name = 'Family')

#get_heatmap(df_map_fish, motifs = True, feature_set = ['known', 'exhaustive'], datatype = 'presence', show_all = True)
plot_embeddings(df_fish.glycan.values.tolist(), label_list = df_fish.Family.values.tolist())
