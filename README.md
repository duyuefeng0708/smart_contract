# Introduction
This project targets the ubiquitous keyword search function and aim to deliver encrypted search services for blockchain-based applications. Specifically, we provide two encrypted search services for private blockchain and public blockchain respectively. Both services ensure the data and query confidentiality without affecting the correctness and verifiability of blockchain, and the service for public blockchain further considers malicious threats in an untrusted distributed environment.

# Publication
Chengjun Cai, Jian Weng, Xingliang Yuan, Cong Wang, “Enabling Reliable Keyword Search in Encrypted Decentralized Storage with Fairness ”, under major revision of IEEE Transactions on Dependable and Secure Computing (TDSC)

Shengshan Hu, Chengjun Cai, Qian Wang, Cong Wang, Luo Xiangyang, and Kui Ren, “Searching an Encrypted Cloud Meets Blockchain: A Decentralized, Reliable and Fair Realization”, in the 37th International Conference on Computer Communications (INFOCOM’18)



# Requirements
Recommended environment for private blockchain network: 

    2 AWS EC2 nodes using t2.medium (2 vCPU, 4 GB RAM ) with operating system Ubuntu 16.04 LTS.

Recommended Public blockchain test network:

    Rinkeby

Required tools:

    ethereum(geth) and truffle
    Python 3.7 
    Python packages: Cryptography and BitVector

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

Put contract file (e.g., Mycontract.sol) into the truffle suite, i.e., into the folder 'contracts'. 

Make sure it is authenticated in the geth console 
    
    > geth attach
    > personal.unlockAccount(eth.coinbase, PASSWORD, 0)
    > exit

Use the truffle command 'migrate' to deploy our contract to the blockchain network

    $ truffle migrate 


# Dataset
We use two datasets to test encrypted search service on private blockchain and public blockchain respectively.

Enron Email Dataset (CMU)

Synthetic financial dataset (with specification provided by Hong Kong Applied Science and Technology Research Institute (ASTRI)

# Execution examples for Application I

### Formatting input dataset

For a financial dataset with 128-dimensional vectors, we first extract each row as a separate file. The keyword inside each file is represented as
    
    attribute:value

For example, keyword 'UID:1' is built with attribute 'UID' and its value in that specific row, i.e., '1'.

We can then put all formatted files into a folder

### Building encrypted index    

The encrypted index is built with python file 'index.py'

    $ python index.py <Folder> 

The built index is stored in the json file 'label.json'

The relation between filename and file id can be found in 'fileid.txt' in <Folder>

### Store built encrypted index to the blockchain

We load the 'label.json' and send the encrypted index them as transactions to the blockchain via javascript file 'StoreIndex.js'

We execute the command with the truffle suite 

    $ truffle exec DSSE/StoreIndex.js

### Generating encrypted search token

Given a plaintext keyword input, we generate the corresponding encrypted search token
    
    $ python searchtoken.py <Keyword>

The generated search token is stored in the json file 'searchtoken.json'

### Execute encrypted search on the blockchain

We load the 'searchtoken.json' and send the search token them as a transaction to the blockchain via javascript file 'Search.js'

We execute the command with the truffle suite

    $ truffle exec DSSE/Search.js

The search result is then presented

# Execution examples for Application II

### Generate encrypted file index

Put all formatted files into a folder

Client generates the file index

    $ python client_democ.py <Folder> 

The index digest and set hash(es) of all added file(s) are presented in the console log, and they will then be recorded on the blockchain via contract function 'Storeindex' 

The built file index is stored as binary file 'fileindex-demo.p'

### Service peer confirms index digest and set hash(es) 

Service peer load the file 'fileindex-demo.p', and execute 'service_peer_check.py' 

    $ python service_peer_check.py <File>

The computed index digest and set hash(es) of all added file(s) are presented and  recorded on the blockchain via contract function 'Storeindex'

If client and service peer have confirmed on the same index digest and set hash(es), the process continues. Otherwise, the process aborts. 

### Generate encrypted search token 

Given a query keyword, client generates the encrypted search token

    $ python searchtoken_demo.py <Keyword>

The generated search token is presented in the console and recorded on the blockchain via contract function 'Search'

### Execute encrypted search 

Service peer loads the search token and execute search operation

    $ python service_peer_democ.py <Search Token>

The search result and result digest are presented on the console, and service peer will record the result digest to the blockchain via contract function 'Search'
