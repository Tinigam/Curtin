#!/bin/bash

year=$1
month=$2

plot_dir="plot_${year}_${month}"
mkdir "$plot_dir"

cp weather_workflow.sh "$plot_dir"
cp plotcmd.txt "$plot_dir"

cd "$plot_dir"

wget --user-agent="Mozilla" "http://www.bom.gov.au/climate/dwo/${year}${month}/text/IDCJDW6111.${year}${month}.csv"
grep "${year}-${month}-" IDCJDW6111.${year}${month}.csv > data.csv
awk -F "," '{print $3, $4, $11, $17}' data.csv > data4.csv

gnuplot --persist plotcmd.txt
gnuplot -e "set terminal png size 400,300; set output 'plot.png'; plot for [col=1:4] 'data4.csv' using 0:col with lines"