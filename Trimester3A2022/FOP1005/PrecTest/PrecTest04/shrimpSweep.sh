#!/bin/bash
# Prac Test 4 - Parameter sweep driver code

low_pop=$1
hi_pop=$2
step_pop=$3

echo "Parameters are: "
echo "Population : " $low_pop $hi_pop $step_pop
outfile="shrimp_pop"$low_pop"-"$hi_pop".csv"
echo "Initial Population,Final Population" > $outfile

for p in `seq $low_pop $step_pop $hi_pop`;
do
    echo "Experiment: " $p
    # Add code here to call shrimpBase.py with the relevant arguments
    # and redirect the output to outfile
    python shrimpBase.py --numOfShrimp "$p" --show_plot "N" >> $outfile
done
