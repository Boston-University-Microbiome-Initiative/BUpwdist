"""
Compute pairwise distances on all samples for a given feature matrix

Author: msilver4@bu.edu
"""

from argparse import ArgumentParser, RawTextHelpFormatter
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import PAIRWISE_DISTANCE_FUNCTIONS
from scipy.spatial.distance import _METRICS_NAMES
import pandas as pd


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('-i', help='Path to feature matrix dataframe CSV [ features (ex. OTUs) X samples ]', required=True)

    pwdist_fncs = sorted(list(set(list(PAIRWISE_DISTANCE_FUNCTIONS.keys()) + _METRICS_NAMES + ['weighted_unifrac', 'unweighted_unifrac'])))
    parser.add_argument('-m', help='Metric. Use a metric from the list here:\n'
                                   'https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html\n'
                                   '\t\tor:\n'
                                   '\t- weighted_unifrac\n'
                                   '\t- unweighted_unifrac',
                        choices=pwdist_fncs, required=True)
    parser.add_argument('-d', help='Path to tree file for unifrac.\n'
                                   'Default: /projectnb/talbot-lab-data/msilver/ref_db/SILVA_132_QIIME_release/trees/99/99_otus.tre',
                        default='/projectnb/talbot-lab-data/msilver/ref_db/SILVA_132_QIIME_release/trees/99/99_otus.tre')
    parser.add_argument('-t', help='Number of threads (default: all)', default=-1)
    parser.add_argument('-o', help='Path to output', required=True)

    args = parser.parse_args()

    # Load table
    df = pd.read_csv(args.i)
    samples = df.columns

    # Compute pairwise distances
    dists = pairwise_distances(df.T, n_jobs=args.t)

    # Place into dataframe
    dist_df = pd.DataFrame(dists, samples, samples)

    # Save
    dist_df.to_csv(args.o)
