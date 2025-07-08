from glycowork.motif.annotate import annotate_glycan, annotate_dataset, quantify_motifs
from glycowork.glycan_data.loader import df_glycan, df_species
import pandas as pd

def count_motifs_per_species(df_glycan: pd.DataFrame, condense: bool = True) -> pd.DataFrame:
    """
    Annotate glycans with motifs and count motif occurrences grouped by species.

    Parameters:
        df_glycan (pd.DataFrame): DataFrame with at least two columns:
                                  - 'glycan': IUPAC-condensed glycan sequences
                                  - 'Species': species names (can contain commas)
        condense (bool): Whether to drop motifs that don't appear in any glycan

    Returns:
        pd.DataFrame: Motif counts per species
                      Rows = species, Columns = motifs
    """
    # Extract glycan sequences and clean species names
    df_sp = df_glycan["Species"].apply(lambda x: str(x).split(",")[0].strip())

    df_gly = df_glycan["glycan"]

    # Annotate motifs in glycans
    df_motif = annotate_dataset(df_gly.tolist(), condense=condense)

    # Set species as index to group later
    df_motif.index = df_sp.values

    # Group by species and sum motif counts
    df_sp_motif_counts = df_motif.groupby(df_motif.index).sum()

    return df_sp_motif_counts

df_sp_motif_counts = count_motifs_per_species(df_glycan)
print(df_sp_motif_counts.head())