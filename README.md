# BUpwdist
Pairwise distance calculation in parallel on SCC

Provide a feature matrix that is [features X samples], like an OTU table:

| otu | Sample 1 | Sample 2 | ... |
| --- | --- | --- | --- |
| otu1 | 3 | 0 | ... |
| ... | ... | ... | ... |

# Documentation
Add an environment variable to the code in your `.bashrc` (only do this once!):
```bash
echo "export pwdist=/projectnb/talbot-lab-data/msilver/BUpwdist" >> ~/.bashrc
```
Input arguments

    $   python pairwise.py -h
    usage: pairwise.py [-h] -i I -m
                       {braycurtis,canberra,chebyshev,cityblock,correlation,cosine,dice,euclidean,hamming,haversine,jaccard,jensenshannon,kulsinski,l1,l2,mahalanobis,manhattan,minkowski,nan_euclidean,precomputed,rogerstanimoto,russellrao,seuclidean,sokalmichener,sokalsneath,sqeuclidean,unweighted_unifrac,weighted_unifrac,wminkowski,yule}
                       [-d D] [-t T] -o O
    
    optional arguments:
      -h, --help            show this help message and exit
      -i I                  Path to feature matrix dataframe CSV [ features (ex. OTUs) X samples ]
      -m {braycurtis,canberra,chebyshev,cityblock,correlation,cosine,dice,euclidean,hamming,haversine,jaccard,jensenshannon,kulsinski,l1,l2,mahalanobis,manhattan,minkowski,nan_euclidean,precomputed,rogerstanimoto,russellrao,seuclidean,sokalmichener,sokalsneath,sqeuclidean,unweighted_unifrac,weighted_unifrac,wminkowski,yule}
                            Metric. Use a metric from the list here:
                            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html
                                            or:
                                    - weighted_unifrac
                                    - unweighted_unifrac
      -d D                  Path to tree file for unifrac.
                            Default: /projectnb/talbot-lab-data/msilver/ref_db/SILVA_132_QIIME_release/trees/99/99_otus.tre
      -t T                  Number of threads (default: all)
      -o O                  Path to output
Run a local job: Use `python $pwdist/pairwise.py -h` to view input arguments (like above). Local runs require having `sklearn`, `skbio`, `scipy`, and `pandas` installed *or* activating my conda environment (which has these) with:
```bash
module load miniconda
conda activate /projectnb/talbot-lab-data/msilver/.conda/envs/msilver
```

Run a batch job on the SCC, uses same input flags as local job: `qsub -pe omp <number of threads> -P <BU project name> $pwdist/pairwise.qsub <path to feature matrix> <metric> <output path>`

Notes:
- Inputs are assumed to be OTU table formatted: each row is a feature (OTU) and each column is a sample, except the first column which contains the feature name.
- Submitting input matrices with null values can cause errors with some metrics or have unintended consequences with others. You can fill null values with the `-f` input flag.