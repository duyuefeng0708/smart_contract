#!/bin/sh
cd $HOME/Desktop/smart_contract/public
read -p "Please input the directory that contains all the files to build file index. `echo $'\n> '`" ans
python3 client_democ.py $ans