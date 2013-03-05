#!/usr/bin/python
import re
import pickle
# generates a list of dictionary objects

# objects look like this
# {
# "species":"human",
# "chr_start": 83469258,
# "chr_end": 83469300,
# "chr": 15,
# "expression": true, # true is posititive for expression
# "sequence" : the genome sequence
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
            m=re.search(">\s*(Human|Mouse)\s*\|\s*chr(\d+):(\d+)-(\d+)\s*\\|\s*element (\d+)\s*\\|\s*(negative|positive)\s*(\\|(.*))?",line)
            if m is not None:
                cur_trial={}
                cur_seq=""

                species=m.group(1)
                chrom=m.group(2)
                chr_start = m.group(3)
                chr_end = m.group(4)
                element = int(m.group(5))
                expression = m.group(6) == 'positive'

                cur_trial["species"]=species
                cur_trial["chr"]=chrom
                cur_trial["chr_start"]=chr_start
                cur_trial["chr_end"]=chr_end
                cur_trial["element"]=element
                cur_trial["expression"] = expression
                results={}
                if expression:
                    for m2 in re.finditer("\s*([^\\|]+?)\\[(\d+)/(\d+)\\]", m.group(8)):
                        result={}
                        result["successes"]=int(m2.group(2))
                        result["total"]=int(m2.group(3))
                        results[m2.group(1)]=result;
                cur_trial["results"]=results

        elif re.match("^\s*$",line) is not None:
            # endline
            if cur_trial.has_key("element"):
                cur_trial["sequence"]=cur_seq.upper()
                trials.append(cur_trial)
        else:
            # sequence line
            cur_seq += line[:-1]
    if cur_trial.has_key("element"):
        cur_trial["sequence"]=cur_seq.upper()
        trials.append(cur_trial)
    return trials


# takes in the vista data generated from extract_vista_data
# takes in the species you are looking at (human, mouse)
# gives you back all the different body parts that experession was seen in
def getBodyParts(vd,species):
    body_parts={}
    for trial in vd:
        if trial["species"]==species :
            for body_part in trial["results"]:
                body_parts[body_part]=True
    return body_parts.keys()



vista_file= "../data/vista_db.txt"
vd = extract_vista_data(vista_file)

pickle.dump(vd,open("../data/vista_data.p","wb"))
