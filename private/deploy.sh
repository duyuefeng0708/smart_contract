#!/bin/sh
echo 'Please make sure the private chain client is running.'

cd $HOME/Desktop/smart_contract/private

truffle network --clean
truffle migrate