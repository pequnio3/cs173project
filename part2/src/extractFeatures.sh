#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
    then
    echo "usage: extractFeatures data_dir vista.pickle chrom.sizes body_part"
else

    data_dir=$1
    vista_pickle=$2
    chrom_sizes=$3
    body_part=$4

    bp_dir=$data_dir/$body_part
    echo $bp_dir

    
    labels=$bp_dir/$body_part.labels

    wig=$bp_dir/wig.wig
    bigwig=$bp_dir/bigwig.bw
    wigs=`cat ../data/brain_wigs.txt`
    out=$bp_dir/$body_part.fv
    features=$bp_dir/temp.fv
    regions=$bp_dir/regions.bed
    rm -rf $bp_dir
    mkdir $bp_dir

    python generateLabels.py $vista_pickle $body_part $out
    python generateBed.py $vista_pickle $regions

 

    count=0
    for wig_loc in $wigs
      do

       wget -O $wig.gz $wig_loc
       gunzip $wig.gz

       /afs/ir/class/cs173/bin/i386_linux26/wigToBigWig $wig $chrom_sizes $bigwig
       rm $wig
       /afs/ir/class/cs173/bin/i386_linux26/bigWigAverageOverBed $bigwig $regions $features
       
       paste -d ' '  $out <(cat $features | awk 'BEGIN{count='$count'*5}{ printf("%i:%f %i:%f %i:%f %i:%f %i:%f\n",count,$2,count+1,$3,count+2,$4,count+3,$5,count+4,$6) }') > $out.temp
       mv $out.temp $out
       rm $features
       count=$count+1
    done

fi