mkdir exp1
cp plotcmd.txt exp1
cd exp1
mkdir run1
mkdir run2
wget --user-agent="Mozilla" http://www.bom.gov.au/climate/dwo/202203/text/IDCJDW6111.202203.csv
grep 2022-03- IDCJDW6111.202203.csv > data.csv
awk -F "," '{print $3, $4, $11, $17}' data.csv > data4.csv
gnuplot --persist plotcmd.txt