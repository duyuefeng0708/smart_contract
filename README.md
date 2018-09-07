# Introduction
This project targets the ubiquitous keyword search function and aim to deliver encrypted search services for blockchain-based applications. Specifically, we provide two encrypted search services for private blockchain and public blockchain respectively. Both services ensure the data and query confidentiality without affecting the correctness and verifiability of blockchain, and the service for public blockchain further considers malicious threats in an untrusted distributed environment.

# Publication
Chengjun Cai, Jian Weng, Xingliang Yuan, Cong Wang, “Enabling Reliable Keyword Search in Encrypted Decentralized Storage with Fairness ”, under major revision of IEEE Transactions on Dependable and Secure Computing (TDSC)

Shengshan Hu, Chengjun Cai, Qian Wang, Cong Wang, Luo Xiangyang, and Kui Ren, “Searching an Encrypted Cloud Meets Blockchain: A Decentralized, Reliable and Fair Realization”, in the 37th International Conference on Computer Communications (INFOCOM’18)



# Requirements
Recommended environment for private blockchain network: 

    2 AWS EC2 nodes using t2.medium (2 vCPU, 4 GB RAM ) with operating system Ubuntu 16.04 LTS.

Recommended Public blockchain test network:

    Rinkeby

Required tools:

    ethereum(geth) and truffle

 Python version and packages:

    Python 3.7 
    Packages: Cryptography and BitVector

# Configuration of private blockchain network
  * Geth genesis.json template

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

# Contract deployment
Make sure it is authenticated first in the geth console, then use the truffle suite.

    > personal.unlockAccount(eth.coinbase, PASSWORD, 0)
    $ truffle compile
    $ truffle migrate

# Dataset
We use two datasets to test encrypted search service on private blockchain and public blockchain respectively.

Enron Email Dataset (CMU)
Synthetic financial dataset (with specification provided by Hong Kong Applied Science and Technology Research Institute (ASTRI)

# Contract function execution examples

For private blockchain:

Store built encrypted index to the blockchain

    $ truffle exec DSSE/StoreIndex.js

Execute encrypted search on the blockchain

    $ truffle exec DSSE/Search.js

For public blockchain :

Generate encrypted file index of added file(s)

    $ python client_democ.py <Folder> 

Confirm index digest and set hash

    $ python service_peer_check.py    

Generate encrypted search token of a query keyword

    $ python searchtoken_demo.py <Keyword>

Execute encrypted search 

    $ python service_peer_democ.py

# License
MIT