#!/usr/bin/python
import re

# generates a list of dictionary objects

# objects look like this
# {
# "species":"human",
# "chr_start": 83469258,
# "chr_end": 83469300,
# "chr": 15,
# "expression": true, # true is posititive for expression
# "element" : 43, # element 43 should be in position 42 in the list
# "trials" : { "body_part1" : {"total":10, "successes":7}, "<body part2>": {"total":4, "successes":}}
#

# example
# a=extract_vista_data("../data/vista_db.txt")

def extract_vista_data(vista_filename):
    f = open(vista_filename,'r')
    trials=[]
    cur_trial={}
    cur_seq=""
    for line in f:
        if line[0]=='>':
            m=re.search(">\s*(Human|Mouse)\s*\|\s*chr(\d+):(\d+)-(\d+)\s*\\|\s*element (\d+)\s*\\|\s*(negative|positive)\s*\\|*(.*)",line)
            if m is not None:
                cur_trial={}
                cur_seq=""

                species=m.group(1)
                chrom=m.group(2)
                chr_start = m.group(3)
                chr_end = m.group(4)
                element = int(m.group(5))
                expression = True if m.group(6) == 'positive' else False
                cur_trial["species"]=species
                cur_trial["chr"]=chrom
                cur_trial["chr_start"]=chr_start
                cur_trial["chr_end"]=chr_end
                cur_trial["element"]=element
                results={}
                for m2 in re.finditer("((\w+\s*)+)\\[(\d+)/(\d+)\\]", m.group(7)):
                    result={}
                    result["successes"]=int(m.group(3))
                    result["total"]=int(m.group(4))
                    results[m.group(1)]=result;
        elif re.match("^\s*$",line) is not None:
            # endline
            if cur_trial.has_key("element"):
                cur_trial["sequence"]=cur_seq
                trials.append(cur_trial)
        else:
            # sequence line
            cur_seq += line[:-1]
    return trials


