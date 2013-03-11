#!/usr/bin/python

import kmers, IO

# Given a kMer determine the coordinate at which it corresponds to the feature vector.
# ------
# In particular, we assume that there is a minimum length of k-mers that were searched over the DNA sequence. 
# So if len(seq) = n, we keep coordinates for all the k-mers with length between min_k and n.
# Thus the implied feature vectors have dimensions = 4^min_k + ... + 4^n-1 + 4^n-2 + 4^n.
# ------

def kmerToPos(min_k, seq):
        
    n = len(seq)
    loc =  0
    
    
    for i in xrange(min_k, n):        
        loc += pow(4,i)
    
    maxLoc = loc  #used for assertion reasons
    
    for i in xrange(0,n):
        place = (n-1)-i
        if seq[place] == 'A':
            loc += pow(4,i) * 0
        elif seq[place] == 'T':
            loc += pow(4,i) * 1
        elif seq[place] == 'G':
            loc += pow(4,i) * 2
        else:
            loc += pow(4,i) * 3
        
    assert (loc < (4**n + maxLoc))
    return loc


def convertToBase(number, base):
    '''
    Input: 2 positive integers: number, base
    Output: The number expressed in a base-system numbering.
    '''
    add = number % base
    if number<=base:
        return str(number)
    else:
        return str(convertToBase(number//base, base)) + str(add)


def posTokMer(min_k,position):    
    '''
    Input: a non-negative integer 'position':
    Output: the kMer that corresponds to the 'position' coordinate of the feature vector.
    '''    
    assert (position >= 0)

    n = min_k
    # loc is the botom of the range given n being the kmer at  pos's length
    loc =0 
    # while loc + its range  doesnt emcompass the position
    while loc + pow(4,n)-1 < position:
        loc += pow(4,n)
        n+=1
    bases="ATGC"
    rel_pos = position- loc
    k=rel_pos

    kmer="A"*n
    if k ==0:
        return kmer
    i=n-1
    while i>=0:
        rem =int(k)%4
        kmer=kmer[0:i]+bases[rem]+kmer[i+1:]
        k=k/float(4)
        i-=1
    return kmer



# writes to outfile a series of feature vectors prepared for libsvm
# based on the species and bodypart
# the index of a feature can be linked to a specific kmer
# the label is 1 if expression is positive 

def extractFeatures(vd, species, body_part, outfile, directions = "onlyStrictNegatives", verbose = True):
    if verbose:
        totalPositive = totalNegative = 0
        print  species + " - " + body_part
        
    f = open(outfile, "w")    
    start_kmer=6
    end_kmer=6

    # size of feature vector
    m = 0
    for k in range(start_kmer,end_kmer+1):
        m += pow(4,k)

    for trial in vd:
        if trial['species'] != species: continue
        
        out = classifyTrial(trial, body_part, directions)
        if out == "skip":
            continue
        
        if verbose:
            if out == "1":
                totalPositive += 1
            else: 
                totalNegative += 1
        
        features = dict()
        
        for k in xrange(start_kmer,end_kmer+1):
            sequence = trial["sequence"]
            kcounts = kmers.computeKmerCounts(sequence,k)
            for kmer in kcounts:
                i = kmerToPos(start_kmer, kmer)
                count = kcounts[kmer]
                features[i] = count
        
        out = out + " "
        for i in sorted(features.iterkeys()):
                
                out+=str(i+1)+":"+str(features[i])+" "    #Added +1 so that feature indices start from 1
                            
        out+="\n"        
        f.write(out)                

    f.close()

    if verbose:
            print "Positive: " + str(totalPositive) + " Negative: " + str(totalNegative) +"."



# Positive = 1, Negative = 0, Not useful = "skip"
def classifyTrial(trial, body_part, directions = "onlyStrictNegatives"):
    isPos   = trial["expression"]
    results = trial["results"]

    if body_part == "any":    #a unified way to deal when we do Not care about where expression occurred.
        if isPos: return "1" 
        else: return "0"
    
    if isPos and body_part in results:  #when taking into account body_part, positive is iff body part has expressed.
        return "1"
    
    #about the Negatives we will decide based on the 'directions'
    if directions == "onlyStrictNegatives":
        if not isPos:
            return "0"
        else:
            return "skip"   #there was expression in some other bodyPart

    else: #will classify as negative -anything- that hasn't expressed the particular bodyPart
        return "0"



if __name__ == '__main__':
    import os, sys, cPickle, simpleStatistics

    vd = cPickle.load( open("../data/vista_db.data","r") )
    
    species     = ["Human","Mouse"]
    body_parts  = ["limb", "neural_tube", "cranial_nerve", "hindbrain", "midbrain", "forebrain", "heart", "any"]

    # Extract features
    for s in species:
        for b in body_parts:
                        
            out = "../data/" + s + "_" + b + "_RN.txt"                    
            extractFeatures(vd, s, b, out, directions="relaxed")
            
#           #TODO fix the sys.path.append("/opt/local/bin/")
#           #Scale feature vectors values to be in [0, 1]            
#            command = "/opt/local/bin/svm-scale -l 0 -u 1 " + out + " > " + out + "_scaled.txt"
#            os.system(command)
#            os.system("rm " + out)

            os.system("python ./checkdata.py " + out)   #call checkdata to verify that format is right for libSVM
            