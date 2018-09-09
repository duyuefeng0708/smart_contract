pragma solidity ^0.4.18;


contract TDSC_demo {
    
    uint80 constant None = uint80(0);
    struct Client {
        
        uint deposit;
        string token;
        string indexdigest;
        uint256[] sethash;
    }
    struct ServicePeer {
        
        uint monetization;
        string token;
        string indexdigest;
        uint256[] sethash;
        uint256 resultdigest;

    }

    
    uint256 searchfee =20;
    uint8 t;
    address CLIENT= 0x470DCff92Ee23EEc68487FB7758a8dbf4C9F894D;
    address SERVICEPEER = 0x7ca5c1511695Cd1372157188BC399Da6C5Aeb942;
    bool searchop = false; // prevent replay attack
    //bool paysearch;   // defined after the judge procedure


    mapping(address => Client) client;
    mapping(address => ServicePeer) servicepeer;
    mapping(address => uint256) public balanceOf;
   
    
    /* This generates a public event on the blockchain that will notify clients */
    function Storeindex(string indexdigest, uint256[] sethash) public returns (uint){
        uint confirmed = 0;
        Client storage owner = client[CLIENT];
        ServicePeer storage worker = servicepeer[SERVICEPEER];
        if (msg.sender==CLIENT){
            //assert(owner.deposit >= searchfee);
            owner.indexdigest = indexdigest;
            owner.sethash = sethash;
            //searchop=true;
            //paysearch = true;
            //return owner.token;
        }
        if (msg.sender==SERVICEPEER){
            //assert(owner.deposit >= searchfee);
            worker.indexdigest = indexdigest;
            worker.sethash = sethash;
            //searchop=true;
            //paysearch = true;
            //return owner.token;
            assert(stringsEqual(owner.indexdigest, worker.indexdigest));
            for (uint i = 0; i< sethash.length; i++){
                assert(owner.sethash[i]==worker.sethash[i]);
                
            }
            confirmed =1;
            return confirmed;
        }
        
    }
    
    // Issue t-locked payment for each search operation
    function Search(string token, uint256 sethash) public returns (bool){
        Client storage owner = client[CLIENT];
        ServicePeer storage worker = servicepeer[SERVICEPEER];
        if (msg.sender==CLIENT){
            //assert(owner.deposit >= searchfee);
            owner.token = token;
            searchop=true;
            //paysearch = true;
            //return owner.token;
        }
        if (msg.sender==SERVICEPEER && searchop == true){
            //paysearch = stringsEqual(owner.token, token);
            assert(stringsEqual(owner.token, token)); // determine if token = \tau_w
            worker.resultdigest = sethash; // store the integrity proof
            //owner.deposit -= searchfee;  // freeze searchfee
            //worker.monetization += searchfee;
            //return (owner.deposit, worker.monetization);
        
    }
}
    
    // Finaiize the payment if the payment has not been revoked
    

    function stringsEqual(string memory _a, string memory _b) pure internal returns (bool) {
    bytes memory a = bytes(_a);
    bytes memory b = bytes(_b);
    if (a.length != b.length)
        return false;
    // @todo unroll this loop 
    for (uint i = 0; i < a.length; i ++)
        if (a[i] != b[i])
            return false;
    return true;
}
}