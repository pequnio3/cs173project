#!/usr/bin/python


import vista_data_reader
import kmers
import array


# given a kmer determines what position in the array it is
def kmerToPos(min_k,seq):
    n= len(seq)
    loc=0
    for i in range(min_k,n):
        loc+= pow(4,i)
    for i in range(0,n):
        place = (n-1)-i
        if seq[place] == 'A':
            loc += pow(4,i)* 0
        elif seq[place] == 'T':
            loc += pow(4,i) *1
        elif seq[place] == 'G':
            loc += pow(4,i) *2
        else:
            loc += pow(4,i) *3
    return loc

# writes to outfile a series of feature vectors prepared for libsvm
# based on the species and bodypart
# the index of a feature can be linked to a specific kmer
# the label is 1 if expression is positive 

def extractFeatures(vd,species,body_part,outfile):
    f =open(outfile,"w")
    data=[]
    start_kmer=6
    end_kmer=6

    # size of feature vector
    m = 0
    for k in range(start_kmer,end_kmer+1):
        m += pow(4,k)

    for trial in vd:
        isPos = doesExpressionOccur(trial,body_part)
        results = trial["results"]
        out =  "1 " if isPos  else  "0 "
        for k in range(start_kmer,end_kmer+1):
            sequence = trial["sequence"]
            kcounts = kmers.computeKmerCounts(sequence,k)
            for kmer in kcounts:
                i = kmerToPos(start_kmer,kmer)
                count = kcounts[kmer]
                out+=str(i)+":"+str(count)+" "        
        out+="\n"
        f.write(out)

# returns true if expression occurs in the given bodypart in the given trial
def doesExpressionOccur(trial, body_part):
    isPos = trial["expression"]
    results = trial["results"]
    if isPos:
        if body_part not in results:
           isPos = False
        else:
            result = results[body_part]
            isPos = result["successes"]/float(result["total"]) >0.5
    return isPos

            
            


vista_file= "../data/vista_db.txt"
vd = vista_data_reader.extract_vista_data(vista_file)
extractFeatures(vd,"human","neural tube","neural_tube.txt")

            
    
