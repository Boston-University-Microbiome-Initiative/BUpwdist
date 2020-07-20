# BUpwdist
Pairwise distance calculation in parallel on SCC

Provide a feature matrix that is [features X samples], like an OTU table:

| otu | Sample 1 | Sample 2 | ... |
| --- | --- | --- | --- |
| otu1 | 3 | 0 | ... |
| ... | ... | ... | ... |

# Documentation
Add an environment variable to the code in your `.bashrc` (only do this once!):
`echo "export pwdist=/projectnb/talbot-lab-data/msilver/BUpwdist/ >> ~/.bashrc`

Distance metrics: Available metrics can be viewed with `python $pwdist/pairwise.py -h` under the `-m` option. The `unifrac` metrics require a tree reference that represents your features. The default tree is the SILVA_132 99% clustered OTUs, located at: `/projectnb/talbot-lab-data/msilver/ref_db/SILVA_132_QIIME_release/trees/99/99_otus.tre`

Run a local job: Use `python $pwdist/pairwise.py -h` to view input arguments

Run a batch job on the SCC: `qsub -pe omp <number of threads> -P <BU project name> $pwdist/pairwise.qsub <path to feature matrix> <metric> <output path>`

Notes:
- Inputs are assumed to be CSVs
- Submitting input matrices with null values can cause errors with some metrics or have unintended consequences with others