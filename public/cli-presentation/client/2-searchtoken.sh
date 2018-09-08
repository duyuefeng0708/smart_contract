#!/bin/sh
cd $HOME/Desktop/smart_contract/public
read -p "Please input the keyword to generate the search token. `echo $'\n> '`" ans
python3 searchtoken_demo.py $ans