# Methods

## Overview architecture
- file in draw.io: 
https://app.diagrams.net/#G1mFBUYRrosRlxSseDJYl_4jQUn8YNE-wJ


## Common0: sequence taxa is not in the top 3 assignment of the cluster

Files location: `/Users/hbagheri/Downloads/nr_taxa`

BoaG query Data:
```text
# cluster information
less boag-job82-output.txt_converted

10000001:1076524=1;1524468=1;666685=1
10000002:348824=2;379=1;501024=3
10000003:1500301=1;1909294=2
10000004:1500301=1;1909294=1

```
Then, we run `seq_clstr_conflict.py` to check if the sequence assignment has conflict with the cluster.

- cluster:taxa_lsit in this file: `boag-job82-output.txt_converted`
- sequence.taxa_list in this file: `nr_single_taxa_converted`
- index file seq:cluster in this file: `95-part-r-00000clustr-seq`


##### convert the query:
```text
python ~/Documents/MyGithub/docs/nr_functions/log_file_converter.py Log_conflicts_all_fix_cluster_with_one_taxa
```
output is: `Log_conflicts_all_fix_cluster_with_one_taxa_converted`, few lines of output:
```text
1AIK {'11676': 1497, '57667': 39, '82834': 12, '11706': 1}
1AK6 {'9606': 16, '9598': 8, '9601': 6, '9823': 1}
1AK8 {'4232': 83, '941927': 76, '214978': 39, '9913': 1}
```



### Results/findings

- What percentage?


## Common1: sequence taxa is in the top 3 assignment of its cluster
File location: `Log_conflicts_all_fix_cluster_with_one_taxa_common1`

The following script generated this file that contains the top1,2, and 3: `exctract_common1.py`

Output for this analysis:
```text
atan-115B-01:nr_taxa hbagheri$ grep "top1" Log_conflicts_all_fix_cluster_with_one_taxa_common1 | wc -l
 36063615
atan-115B-01:nr_taxa hbagheri$ grep "top2" Log_conflicts_all_fix_cluster_with_one_taxa_common1 | wc -l
 15210624
atan-115B-01:nr_taxa hbagheri$ grep "top3" Log_conflicts_all_fix_cluster_with_one_taxa_common1 | wc -l
 5815628

```

**Q: check that these are not clusters with one member.**

For the common1 how to analyze the trust score?

- Q1: if seq taxa is the top (1)? What percentages? What is the CS?
    - for the dictionary that has the top 3; get top 1 and calculate the score.
    - example: `117E 42095340 [('4932', 4)] [('4932', 42), ('559292', 3), ('1095631', 2)]`
    - 

- Q2: if seq taxa is the top (1)? What percentages? What is the CS?

- Q3: if seq taxa is the top (1)? What percentages? What is the CS?

