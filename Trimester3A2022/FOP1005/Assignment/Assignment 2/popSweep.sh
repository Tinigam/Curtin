#!/bin/bash
# Assignment 2 - Parameter sweep driver code

low_human_pop=$1
high_human_pop=$2
low_vampire_pop=$3
high_vampire_pop=$4

data=Graph_$1-$2_$3-$4_dir
mkdir $data
cp A2.py $data
cp popSweep.py $data
cp characters.py $data
cd $data
echo "Parameters are: "
echo "Population : " $low_human_pop, $high_human_pop, $low_vampire_pop, $high_vampire_pop
outfile="Population"$low_human_pop"-"$high_human_pop","$low_vampire_pop"-"$high_vampire_pop".csv"
echo "Initial Human Population,Final Human Population,Initial Vampire Population,Final Vampire Population" >> $outfile
for human_pop in `seq $low_human_pop 10 $high_human_pop`
do
    for vampire_pop in `seq $low_vampire_pop 1 $high_vampire_pop`
    do
        echo "Experiment: " $human_pop $vampire_pop
        python3 A2.py $human_pop $vampire_pop >> $outfile
    done
done

