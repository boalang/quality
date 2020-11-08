# Data Quality of NR database
Improving data quality of  taxonomic assignments in  large-scale public databases


# Method

## Implementation
To run data quality analysis at large-scale, we used BoaG for the computationally expensive part.
Then, we used current library in Python and Jupyter notebook for the postprocessing.

Boag is a domain-specific language and infrastructure on top of Hadoop for genomics data. Website: https://boalang.github.io/bio/

BoaG compiler is written in Java and the source code is available [here](compiler)
* This is a video on step by step instructions to set up programming environment on Eclipse for Boa compiler. [link](https://www.youtube.com/watch?v=s4-xfprwJ0c)

 
### Step1: Script and analysis on BoaG infrastructure

- [BoaG query on list of taxonomic assignments](http://boa.cs.iastate.edu/boag/?q=boa/job/public/80)

- [BoaG query for the taxonomic assignments in NR95 clusters](http://boa.cs.iastate.edu/boag/?q=boa/job/public/82)

### Step2: Postprocessing in Python and Jupyter Notebooks
- [Lineage](notebooks/Lineage.ipynb)
- [Provenance](notebooks/NR_Dataset_Provenance.ipynb)
- [Construct Tree with ETE3 library](notebooks/Tree.ipynb)
- [Identifying conflicts](Python/find_conflicts.py)
    - Output: [List of misclassified sequences](https://drive.google.com/drive/u/3/folders/1cW95cF1n1Ur2NVHRtPUOp8sacyOCPW8Q)
        - This file shows list of conflicts. Sequence ID, Cluster DI, Sequence assignment, top3 assignments of the clusters 
        are shown along with confidence score for the proposed assignment in the next line. See example:
        `1A0Q 55656088 [('10090', 1)] [('562', 24), ('168807', 2), ('405955', 1)] 
         CS=  0.8888888888888888`


## Dataset

#### Clustering information
- [NR95](https://drive.google.com/drive/u/3/folders/10fll7IEcH-FFZku9J0M_KVPzAUXUfRva)
- [NR90](https://drive.google.com/drive/u/3/folders/1kEqskSjcqWz6w6TmBBIS_jifvEsQlQTi)
- [NR85](https://drive.google.com/drive/u/3/folders/1nRiRHh86ED0k5RpLLGGPDyd5ZnszgrYD)
- [NR80](https://drive.google.com/drive/u/3/folders/1-3Y-AT7d-HxLPvcFDcNsnL38U9aOonAf)
- [NR75](https://drive.google.com/drive/u/3/folders/1ml0kOa-h7B1KkkVPNMPvnUuQtbWy_Y36)
- [NR70](https://drive.google.com/drive/u/3/folders/1p9GANq1qPyakdas_bUgIlQjyDh4pXnC6)
- [NR65](https://drive.google.com/drive/u/3/folders/18tyHTeAKd4qJnOFRrYd7nbDpyaX8aFsR)



# Evaluation
### Simulated dataset
- [Link](simulated)

### Manual Analysis
- [Link](manual)

### Literature dataset
Following works on detecting and correcting misclassifications in rRNA sequences.
* https://github.com/amkozlov/mislabels16-data
* https://peerj.com/articles/5030/#supplemental-information

### UniProt --UniRef90 (clusters at 90% sequence similarity)
- The entire dataset 119 million sequences: https://www.uniprot.org/uniref/?query=&fil=identity:0.9

Following are examples of misclassifications in the 90% clusters
```text
root conflict in  UniRef90_I3TC36
cellular organisms conflict UniRef90_I3TC36
superkingdom conflict UniRef90_I3TC36
phylum conflict UniRef90_I3TC36
```


## Figures and charts references
- [Charts in google sheets](https://docs.google.com/spreadsheets/d/16XEiXRGH7UleuuQzU2gg_gpD-0Xkr3RDw09WzFhV8g8/edit#gid=1064192369)
- [Draw.io Algorithm overview](https://app.diagrams.net/#G1mFBUYRrosRlxSseDJYl_4jQUn8YNE-wJ)

