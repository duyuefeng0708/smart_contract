#!/bin/sh
cd $HOME/Desktop/smart_contract/private
echo 'Please make sure the private chain client is running.'

truffle network --clean
truffle migrate