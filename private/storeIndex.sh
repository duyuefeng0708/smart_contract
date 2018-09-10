#!/bin/sh

cd $HOME/Desktop/smart_contract/private

# read -p "Please input the directory that contains all the files to be built. `echo $'\n> '`" ans
ans=$1
# echo $1
cd ./DSSE/buildIndex
python index.py $ans
cd ../
# Mac OS needs -i "" to overwrite using sed, "" should not appear in other Unix-like platforms.
sed "s/finance1/$ans/g" StoreIndexSpare.js > StoreIndex.js
sed "s/finance1/$ans/g" SearchSpare.js > Search.js
cd ../ 
truffle exec DSSE/StoreIndex.js