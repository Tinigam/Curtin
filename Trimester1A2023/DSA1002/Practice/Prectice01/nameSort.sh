#!/bin/bash

sort=$1

outfile=SortedName7000_$1.csv
python3 nameSort.py $sort >> $outfile