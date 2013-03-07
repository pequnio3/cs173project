#!/usr/bin/python

def computeReverseCompliment(s):
    rc_s = s
    rc_s = rc_s.replace("A","1")
    rc_s = rc_s.replace("T","A")
    rc_s = rc_s.replace("1","T")
    rc_s = rc_s.replace("G","1")
    rc_s = rc_s.replace("C","G")
    rc_s = rc_s.replace("G","T")
    rc_s = rc_s[::-1]
    return rc_s

def computeKmerCounts(s,k):
    kmer_counts ={}
    rc_s = computeReverseCompliment(s)
    parts = [s]
    if rc_s != s:
        parts.append(rc_s)
        
    for part in parts:
        for i in range(0,len(part)+1-k):
            kmer = s[i:i+k]
            if kmer in kmer_counts:
                kmer_counts[kmer] = kmer_counts[kmer] + 1
            else:
                kmer_counts[kmer] = 1
    return kmer_counts
