#!/bin/sh

cd $HOME/Desktop/smart_contract/private
# read -p "Please input the keyword to search. `echo $'\n> '`" ans
ans=$1
cd ./DSSE/buildIndex
python searchtoken.py ${ans}
cd ../../
# Mac OS needs -i "" to overwrite using sed, "" should not appear in other Unix-like platforms.
truffle exec DSSE/Search.js > outcome
echo '^'
python readoutput.py | while read line ; do cat ./DSSE/buildIndex/db/finance10/$line ; done
echo '^'