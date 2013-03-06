#!/bin/bash                                                                                                                                                                                              

bodypart=argv[1]
regions=argv[2]
vista_pickle=argv[3]
chrom_sizes=argv[4]

out=$bodypart.fv
labels=(0)
mapping_fn=somepythonfunction
bigwig=bigwig.bw
features=features5.tab
wigs=(wig1 wig2)

for wig_loc in ${wigs[@]}
do
wget $wig_loc
wig=$(basename $wig_loc)
gzip $wig
/afs/ir/class/cs173/bin/i386_linux26/wigToBigWig $wig $chrom_sizes $bigwig
rm $wig
/afs/ir/class/cs173/bin/i386_linux26/bigWigAverageOverBed $bigwig $regions $features
rm $bigwig

#use join to join avg_temp to out                                                                                                                                                                        
done

