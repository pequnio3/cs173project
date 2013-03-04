#!/usr/bin/python

def computeKmerCounts(s,k):
    kmer_counts={}
    for i in range(0,len(s)-k):
        kmer = s[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] = kmer_counts[kmer] + 1
        else:
            kmer_counts[kmer] = 1 
    return kmer_counts
