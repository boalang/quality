#!/usr/bin/python
import sys
import  os
'''
This script converts BoaG output from Hadoop to a easier format to generate tree
 input example:
    count[1A43][11676] = 1
    count[1A43][11698] = 4
    count[1BOB][4932] = 1
    count[1BOB][559292] = 2
    count[1WWW][32630] = 1
    count[1WWW][9606] = 13
    count[xxx][2294] = 14

 output: 
    1A43:11676=1;11698=4
    1BOB:4932=1;559292=2
    1WWW:32630=1;9606=13 
'''

def check_clusters():
    taxSet = set()
    current_id = -1
    txt_row =""
    with open(sys.argv[1], "r") as f, open(sys.argv[1]+"_converted", "w") as converted_file:
        for line in f:
            row_id = line[line.index("[") + 1:line.index("][")]
            tax_id = line[line.index("][") + 2:line.index("] =")]
            tax_count = line[line.index("= ") + 2 :]
            if current_id == -1:
                current_id = row_id
                txt_row = row_id + ":"

            # while the new line is in the same cluster add the tax ids to the set
            if current_id == row_id:
                #TODO: count number of tax ids for each protein or cluster here
                if tax_id != '' and tax_id !='0':
                    taxSet.add(tax_id)
                    txt_row += tax_id+"="+tax_count.rstrip()+";"
            else:
                current_id = row_id
                txt_row = txt_row[:-1]

                # TODO: do we need to ignore those that have only one taxa??
                # This means if the sequence or cluster should have more than one taxa
                if txt_row.count(';') > 0 :
                    converted_file.write(txt_row + "\n")

                txt_row = row_id + ":"
                taxSet.clear()
                if tax_id !='' and tax_id !='0':
                    taxSet.add(tax_id)
                    txt_row += tax_id+"="+tax_count.rstrip()+";"

    txt_row = txt_row[:-1]
    # print(txt_row)
    with open(sys.argv[1] + "_converted", "a") as converted_file:
        if txt_row.count(';') > 0:
            converted_file.write(txt_row+ "\n")

check_clusters()