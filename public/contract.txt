pragma solidity ^0.4.18;

contract SchedulerInterface {

    function scheduleTransaction(address toAddress,
                                 bytes4 callData,
                                 uint8 windowSize,
                                 uint[3] uintArgs) public returns (address);
}

contract tlocked_searchpay {
    
    uint80 constant None = uint80(0);
    struct Client {
        
        uint deposit;
        string token;
    }
    struct ServicePeer {
        
        uint monetization;
        string sethash;

    }

    
    uint256 searchfee =20;
    uint8 t;
    address JUDGE = 0xAE0200eC1EcCc6CCdb2349f6097627Ca9592b87d;
    address CLIENT = 0xfcF590474c6776F1909F50F47f67f6a11cAc6Ec4;
    address SERVICEPEER = 0x2B62b54227B1589Bbd12224a31A81f55211Dc69E;
    address Depositpool = 0x10064182b97A3f8077b1EF1c9612Eef78FE055f0;
    bool searchop = false; // prevent replay attack
    bool paysearch;   // defined after the judge procedure


    mapping(address => Client) client;
    mapping(address => ServicePeer) servicepeer;
    mapping(address => uint256) public balanceOf;
   
    
    /* This generates a public event on the blockchain that will notify clients */
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    /*function scheduleCall(address contractAddress,
                          bytes4 abiSignature,
                          uint targetBlock) public returns (address);
    */
    // SchedulerInterface constant scheduler = SchedulerInterface(0xF423F8031D13bA0830Ece4364Af70D06ddB32DB7);
   
    
    // Client deposit
    function Deposit(uint256 _value) public returns (uint256 ss) {
        assert(msg.sender == CLIENT);
       // assert(balanceOf[msg.sender] >= _value); //check if the client has enough money
        //assert(balanceOf[Depositpool] + _value >= balanceOf[Depositpool]); // check for overfolws
        //balanceOf[msg.sender] -= _value;
        //balanceOf[Depositpool] += _value;
        Client storage owner = client[msg.sender];
        owner.deposit += _value; //update the client deposit state
        return  owner.deposit;
    }
    
    
    function get() view public returns (bool){
        
        return paysearch;
    }
    
    // Issue t-locked payment for each search operation
    function Searchcharge(string token, string sethash) public returns (bool){
        Client storage owner = client[CLIENT];
        ServicePeer storage worker = servicepeer[SERVICEPEER];
        if (msg.sender==CLIENT){
            assert(owner.deposit >= searchfee);
            owner.token = token;
            searchop=true;
            paysearch = true;
            //return owner.token;
        }
        if (msg.sender==SERVICEPEER && searchop == true){
            //paysearch = stringsEqual(owner.token, token);
            assert(paysearch = stringsEqual(owner.token, token)); // determine if token = \tau_w
            worker.sethash = sethash; // store the integrity proof
            owner.deposit -= searchfee;  // freeze searchfee
            worker.monetization += searchfee;
            //return (owner.deposit, worker.monetization);
        
        // Schedule a call to the `Callbacksearch` function after t blocks
         /* uint[3] memory uintArgs = [
            200000,      // the amount of gas that will be sent with the txn.
            0,           // the amount of ether (in wei) that will be sent with the txn
            block.number + t // the first block number on which the transaction can be executed.
        ];
        scheduler.scheduleTransaction(
            address(this),               // the address that should be called.
            bytes4(keccak256("Callbacksearch()")),  // 4-byte abi signature of callback function
            255,          // delay factor
           uintArgs
        );*/
        searchop = false;
    }
}
    // The judgment peer calls this function to revoke the Scheduled payment
    function Judge() public returns (bool){
        assert(msg.sender == JUDGE);
        Client storage owner = client[CLIENT];
        ServicePeer storage worker = servicepeer[SERVICEPEER];
        paysearch = false; // alter the flag
        worker.monetization -=  searchfee; // rewind the deposit state
        owner.deposit += searchfee;
        return paysearch;
    }
    
    // Finaiize the payment if the payment has not been revoked
    function Callbacksearch() public {
        if (paysearch == true){
            uint256 value = searchfee; 
            emit Transfer(Depositpool, SERVICEPEER, value); // the payment is finalized on the ledger
        }
    }

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