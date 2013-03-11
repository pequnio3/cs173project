#!/bin/bash                                                                                                                                                                                              

if [ $# -ne 4 ]
then
    echo "usage: extractFeatures feature_dir regions_file chrom.sizes wig_file"
else

    feature_dir=$1
    regions_file=$2
    chrom_sizes=$3
    wigs_file=$4




    wigs=`cat $wigs_file`

    for wig_loc in $wigs
    do
	feature_name=`basename $wig_loc | sed s/.wig.gz//`

	wig=$feature_dir/$feature_name.wig
	bigwig=$feature_dir/$feature_name.bg

	features=$features_dir/$feature_name.fv

	wget -O $wig.gz $wig_loc
	gunzip $wig.gz

	/afs/ir/class/cs173/bin/i386_linux26/wigToBigWig $wig $chrom_sizes $bigwig
	rm $wig
	/afs/ir/class/cs173/bin/i386_linux26/bigWigAverageOverBed $bigwig $regions_file $features
	rm $bigwig
    done
fi
