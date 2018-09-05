# Introduction
This project is a decentralized SSE design following the similar SSE design originated by Cash et al. (CCS 14), which is deployed among a private blockchain using Amazon Web Service. It enables a user to derive the auditable query result over encrypted data that leaks zero knowledge in the private blockchain setting assuming write capability is restricted to certain organization(s).

# Publication
?

# Requirements
Recommended environment: 

    2 AWS EC2 nodes using t2.medium (2 vCPU, 4 GB RAM ) with default 8G SSD,pick Ubuntu 16.04 LTS.

Major tools:

    geth and truffle

# Installation
Environment setup for each ec2 instance:

    $ apt-get install software-properties-common curl git vim build-essential
    $ add-apt-repository -y ppa:ethereum/ethereum
    $ apt-get update
    $ apt-get install ethereum
    $ curl -sL https://deb.nodesource.com/setup_10.x | -E bash -
    $ apt-get install -y nodejs
    $ npm install -g truffle

# Configuration
  * Geth initialization json template

```json
{
    "config": {
        "chainId": 8888,
        "homesteadBlock": 0,    
        "eip155Block": 0,
        "eip158Block": 0
    },
    "coinbase" : "0x0000000000000000000000000000000000000000",
    "difficulty" : "0x1000",
    "extraData" : "",
    "gasLimit" : "0x7a1200",
    "nonce" : "0x0000000000000042",
    "mixhash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp" : "0x00",
    "alloc": {
    }
}
```

    $ geth init template.json

# Start a private network
Make sure etherbase is different in different ec2 instances.

    $ geth --nodiscover --rpc --rpcport 8545 --mine console --etherbase=0x0000000000000000000000000000000000000000
    > admin.nodeInfo.enode

For the second ec2 instance, add enode address of the first ec2 instance.
    
    > admin.addPeer(<enode>)

# Contract deployment
Make sure it is authenticated first in the geth console. Next use the truffle suite in this truffle project.

    > personal.unlockAccount(eth.coinbase, PASSWORD, 0)
    > exit
    $ truffle compile
    $ truffle migrate

# Dataset
"labeltest1w.json" and "searchtoken.json" are the build SSE database and search index separately and are already available for direct contract call. We suggest using the "test1w" data in the directory ./DSSE/buildIndex/db for SSE-building python scripts, and "test1w" contains a lot emails as the raw data for SSE preparation.

# Contract function call

    $ truffle exec DSSE/StoreIndex.js
    $ truffle exec DSSE/Search.js

# More details
https://medium.com/@duyuefeng0708/set-up-private-blockchain-on-amazon-web-service-via-geth-and-truffle-suite-b0023ddaae69

# License
?