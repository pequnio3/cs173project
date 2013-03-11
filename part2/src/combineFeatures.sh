#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
then
    echo "usage: combineFeatures data_dir vista.pickle body_part features_dir"
else
    
    data_dir=$1
    vista_pickle=$2
    body_part=$3
    features_dir=$4

    # generate a 
    features=`ls $features_dir`

    bp_dir=$data_dir/$body_part
    echo $bp_dir

    
    labels=$bp_dir/$body_part.labels

    out=$bp_dir/$body_part.fv

    rm -rf $bp_dir
    mkdir $bp_dir

    touch $out

    python generateLabels.py $vista_pickle $body_part $out

    count=0
    for feature in $features
    do
	paste -d ' '  $out <(cat $features_dir/$feature | awk 'BEGIN{count='$count'*5}{ printf("%i:%f %i:%f %i:%f %i:%f %i:%f\n",count,$2,count+1,$3,count+2,$4,count+3,$5,count+4,$6) }') > $out.temp
	mv $out.temp $out
	count=$count+1
    done

fi
