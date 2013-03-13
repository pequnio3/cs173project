#!/usr/bin/python    
import sys
import cPickle

def classifyTrial(trial, body_part):
    isPos   = trial["expression"]
    results = trial["results"]
    brain=["midbrain","hindbrain","forebrain","cranial nerve","nerual tube"]
    limb=["limb"]
    heart=["heart"]


    body_parts =[]
    if body_part == "brain":
        body_parts = brain
    elif body_part == "limb":
        body_parts=limb

    elif body_part == "midbrain":
        body_parts=["midbrain"]

    elif body_part == "hindbrain":
        body_parts=["hindbrain"]

    elif body_part == "forebrain":
        body_parts=["forebrain"]

    elif body_part == "cranial_nerve":
        body_parts=["cranial_nerve"]

    elif body_part == "neural_tube":
        body_parts=["neural_tube"]

    elif body_part == "limb":
        body_parts=limb

    elif body_part=="heart":
        body_parts=heart

    elif body_part == "any":
        body_parts=["any"]
    
    is_expression=False
    for bp in body_parts:
        if isPos and bp == "any":    #a unified way to deal when we do Not care about where expression occurred.
            is_expression=True
            break
        elif isPos and bp in results:  #when taking into account body_part, positive is iff body part has expressed.
            is_expression = True
            break
    if is_expression:
        return "1"
    else:
        return "0"



def generateLabels(vd,labels,body_part):
    labels_f = open(labels,'w')
    for trial in vd:
        label = classifyTrial(trial,body_part)+"\n"
        labels_f.write(label)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "usage: generateLabels <vista_data_pickle> <body part> <labels outfile> "
    else:
        vd_p = sys.argv[1]
        body_part = sys.argv[2]
        labels = sys.argv[3]

        vd = cPickle.load( open(vd_p,"r") )
        generateLabels(vd,labels,body_part)
