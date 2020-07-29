#!/bin/bash
#removes comments new lines and html tags from file to only get hard coded data
file=$1
output=$2
sed -r '/^\s*$/d' $file >> tmp.idk
awk -v FS="" '{ for(i=1; i<=NF; i++){if($i$(i+1)$(i+2)$(i+3)=="<!--"){i+=4; p=1} else if(!p && $i!="-->"){printf $i} else if($i$(i+1)$(i+2)=="-->") {i+=3; p=0;} } printf RS}' tmp.idk >> tmp2.idk

cat tmp2.idk | sed 's/$/©/' | tr -d '\n' | sed 's/<script.*<\/script>//g' | sed 's/<[^>]*>//g' | sed 's/©/\n/g' | sed '/^ *$/d' | sed 's/^ *//' >> tmp3.idk
sed -r '/^\s*$/d' tmp3.idk >> $output 
rm tmp.idk tmp2.idk tmp3.idk
