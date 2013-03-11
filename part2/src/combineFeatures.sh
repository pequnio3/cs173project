#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
then
    echo "usage: combineFeatures data_dir wigs_file vista.pickle body_part features_dir"
else
    
    data_dir=$1
    wig_file=$2
    vista_pickle=$3
    body_part=$4
    features_dir=$5

    # generate a 
    wigs=`fn $wigs_file $body_part`

    bp_dir=$data_dir/$body_part
    echo $bp_dir

    
    labels=$bp_dir/$body_part.labels

    out=$bp_dir/$body_part.fv
    touch $out

    rm -rf $bp_dir
    mkdir $bp_dir

    python generateLabels.py $vista_pickle $body_part $out

    count=0
    for wig_loc in $wigs
    do
	feature_name=`basename $wig_loc | sed s/.wig.gz//`
	features=$features_dir/$feature_name.fv
	paste -d ' '  $out <(cat $features | awk 'BEGIN{count='$count'*5}{ printf("%i:%f %i:%f %i:%f %i:%f %i:%f\n",count,$2,count+1,$3,count+2,$4,count+3,$5,count+4,$6) }') > $out.temp
	mv $out.temp $out
	rm $features
	count=$count+1
    done

fi
