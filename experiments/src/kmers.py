#!/usr/bin/python

def reverseComplement(inputStrand):
    reverseStrand = ""
    
    revMap = {"A":"T", "C":"G", "G":"C", "T":"A"}

    for letter in reversed(inputStrand):
        reverseStrand += revMap[letter]
        
    return reverseStrand

def computeKmerCounts(s,k):
    kmer_counts ={}
    rc_s = computeReverseCompliment(s)
    parts = [s]
    if rc_s != s:
        parts.append(rc_s)
        
    for part in parts:
        for i in xrange(0,len(part)+1-k):
            kmer = s[i:i+k]
            if kmer in kmer_counts:
                kmer_counts[kmer] = kmer_counts[kmer] + 1
            else:
                kmer_counts[kmer] = 1
    return kmer_counts