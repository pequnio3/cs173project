#!/usr/bin/python    
import sys
import cPickle



def generateBed(vd,bed):
    bed_f = open(bed,'w')
    count=0
    for trial in vd:

        bed_seq="chr"+trial["chr"]+"\t"+trial["chr_start"]+"\t"+trial["chr_end"]+"\t"+str(count)+"\n"
        bed_f.write(bed_seq)
        count +=1

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage: generateBed <vista_data_pickle> <bed out file>"
    else:
        vd_p = sys.argv[1]
        bed= sys.argv[2]
        vd = cPickle.load( open(vd_p,"r") )
        generateBed(vd,bed)
