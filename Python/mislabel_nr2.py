import sys
import random

"""
this script add a random taxa to the sample of NR; current sample proteins do not have multiple assignment
they only have one distinct taxa

example:
    KUJ96915:1635258=1
    WP_105257249:1307=1
    XP_014680581:37621=1



"""


def mislabel(boa_output):
    protein_taxa_set = set()

    # read full nr taxa from a text file that has one taxa in each line
    nr_taxa_file = "/Users/hbagheri/Downloads/mis-ann/seqCount2019V3/nr_taxa_list_from_Boa"

    with open(nr_taxa_file, "r") as tax_file:
        nr_full_taxa = tax_file.read().splitlines()
        print("nr tax list size:", len(nr_full_taxa))

    mislabel_rank = 'phylum'

    with open(boa_output, 'r') as f, open(boa_output + "_mislabeled", 'w') as mislabeled_file:
        for line in f:
            seq_id = line[:line.index(":")]  # example WP_105257249:1307=1
            # take a random taxa
            random_tax = random.sample(nr_full_taxa, 1)

            # write it in the disk
            # add random_tax=1 to the end
            mislabeled_file.write(seq_id + ":" + random_tax[0] + "=1" + '\n')


# the verified sample is here: '/Users/hbagheri/Downloads/mis-ann/simulated/sample_verified'
mislabel(sys.argv[1])