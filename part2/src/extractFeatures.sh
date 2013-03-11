#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
then
    echo "usage: extractFeatures feature_dir expressors.bed chrom.sizes wigs_file"
else

    features_dir=$1
    expressors_bed=$2
    chrom_sizes=$3
    wigs_file=$4




    wigs=`cat $wigs_file`

    for wig_loc in $wigs
    do
	feature_name=`basename $wig_loc | sed s/.wig.gz//`
	echo "***************"
	echo "extracting: ${feature_name}"
	echo "***************"

	wig=$features_dir/$feature_name.wig
	bigwig=$features_dir/$feature_name.bg 

	features=$features_dir/$feature_name.fv

	echo "downlaoding ${wig}.gz"
	
	wget -q -O $wig.gz $wig_loc

	if [ -s $wig.gz ]
	then
	    
	    echo "extracting ${wig}.gz"
	    gunzip $wig.gz
	    echo "generating big wig ${bigwig}"
	    /afs/ir/class/cs173/bin/i386_linux26/wigToBigWig $wig $chrom_sizes $bigwig
	    rm $wig

	    echo "generating features  ${features}"
	    /afs/ir/class/cs173/bin/i386_linux26/bigWigAverageOverBed $bigwig $expressors_bed $features
	    rm $bigwig
	else
	    echo "xxxxxxx - downloading ${wig}.gz failed."
	    echo "continuing"
	    rm $wig.gz
	fi

    done
fi
