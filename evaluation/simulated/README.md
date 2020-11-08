## Simulated dataset
We randomly assigned a taxa to a sample of 1M sequences and then checked with our approach.
We repeated this experiment three times and reported the average.

- location: `/Users/hbagheri/Downloads/nr_taxa`
- sequence file sample: 
`shuf -n 1000 nr_single_taxa_converted2 > evaluation/simulated/nr_single_taxa_converted2_sample1000`
- few examples: 
 ```text
    KUJ96915:1635258=1
    WP_105257249:1307=1
    XP_014680581:37621=1
 ```

- then, remove the assignment and give a random assignment and then check if we can detect the wrong assignment.
    - Previous work: python code: `mislabel_nr.py` location: `/Users/hbagheri/Downloads/mis-ann/simulated`
        - this code takes different phylum for the current protein and add a random taxa
        - precision and recall
        - FP and FN reason?
    
    - run the experiment and check the conflicts:
     `python ~/Documents/MyGithub/docs/nr_functions/seq_clstr_conflict_old.py  /Users/hbagheri/Downloads/nr_protein_functions/95-part-r-00000clustr-seq  /Users/hbagheri/Downloads/nr_taxa/boag-job82-output.txt_converted  /Users/hbagheri/Downloads/nr_taxa/evaluation/simulated/nr_single_taxa_converted2_sample1000_mislabeled > Log_conflict_sample1000`
        - few lines of the output:
            ```text
              CRL25862 17643229 [('383309', 1)] [('27334', 4), ('5075', 1)]
              common0 CS=  0.8
              PMB75513 49515533 [('1090690', 1)] [('683846', 2), ('1163730', 1)]
              common0 CS=  0.6666666666666666
            
            ```
    - What is the P and R? 
        - based on formula for P=98% and R=95%
            - confusion matrix online: http://onlineconfusionmatrix.com/
        - FP =10: due to the tree error (ETE library error main reason is the ncbi taxa database is changing)
        - FN=50: small clusters, and tree didn't generate due to change in the taxa
