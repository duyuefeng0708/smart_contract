#!/bin/sh
cd $HOME/Desktop/smart_contract/public
value=`cat searchtoken.json`
temp="${value%\"}"
temp="${temp#\"}"
python3 service_peer_democ.py $temp
