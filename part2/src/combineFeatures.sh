#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
then
    echo "usage: combineFeatures data_dir vista.pickle body_part features_dir"
else
    
    data_dir=$1
    vista_pickle=$2

    body_part=`echo $3 | sed "s/ /_/"`
    features_dir=$4
    echo $body_part


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

    let count=0
    for feature in $features
    do
	paste -d ' '  $out <(cat $features_dir/$feature | awk 'BEGIN{c='$count'*5}{ printf("%i:%f %i:%f %i:%f %i:%f %i:%f\n",c,$2,c+1,$3,c+2,$4,c+3,$5,c+4,$6) }') > $out.temp
	mv $out.temp $out
	let count+=1
    done
    sort -k 1,1 -n $out > $out.temp
    mv $out.temp $out
fi
