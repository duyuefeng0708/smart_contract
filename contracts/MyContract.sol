pragma solidity ^0.4.4;
//import "github.com/ethereum/dapp-bin/library/linkedList.sol";

contract MyContract{
//    using DoublyLinkedList for DoublyLinkedList.data;
//    DoublyLinkedList.data public revidlist; // use for storing revids
    
    address master_addr;
    uint  x;
    uint[50] rr;
    bytes32 ipad = 0x3636363636363636363636363636363636363636363636363636363636363636;
    bytes32 opad = 0x5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c;
    
	string str;
	//string[] revidset;
   
    struct Node{
        byte node_byte;
        uint node_int;
    }


//Store index using struct.     
/*    struct Pair{
    	string label;
    	uint id;
    }
    
    Pair[] public index;
*/    

//Store index using mapping.
    mapping (string => bytes32)  index;
    
    mapping (string => uint)  index_add; // ++ Add index ++
    
    mapping (string => uint)  index_del; // ++ revid index ++
    
 	mapping (string => string) test;
 	
 	mapping (string => bytes32)  randomstring;  // ++ random string index ++
 	


    //mapping (uint =>  Node) nodes;
    
    function MyContract () {
 		test['hu']= 'construct';
		test['gyt'] ='tratea';
		x = 888234;


    }
    

	function set (string str1) returns (string,uint) {
		
		test[str1] = 'str1';
		
/*		test['hu']= '122';
		test['gyt'] ='433';
		x = 4567;
	*/
		
		return (test[str1], x);
	}
	
	function read (string str1) returns (string,uint) {
		return (test[str1], x);
	}


/*        
    
//Since contract receives hash values as string type, thus each received hex-type value are regarded as string
//and stored in string's ascii value. Therefore to enable comparison, we first need to transform string into its 
//original ascii value, and then transform contract's generated hash value into uint type, such that we can 
//compare them.
       
//to be continue...         


//here each hash value need to be 32-bytes in length (ie, sha256)
function hashtoascii(bytes32[] hash_input) returns (bytes32,string)  {
		
		uint memory hashlength =32;
		
		string memory temp;
		temp = Bytes32toString(hash_input);
		
	
		
		uint  left;
		uint  right;
		uint  value;
		uint  counter1 = 0;
		
		
		uint[32] memory  combine;

		uint counter2=0;  //which row stores in label
		
		for(uint i=0; i<hash_input.length;i=i+2){
		
			
			counter1 = 0; //which colunm stores in label
			
			for(uint j=0; j<hashlength; j=j+2){
			
				left = uint(hash_input[i][j]);
				right = uint(hash_input[i][j+1]);
				
				left = strtoascii(left);
				right = strtoascii(right);
				
								
				value =left *16 + right;
			
				label[counter2][counter1] = value;
				counter1++;
			}
		
			for( j=0; j<hashlength; j=j+2){
			
				left = uint(hash_input[i+1][j]);
				right = uint(hash_input[i+1][j+1]);
				
				left = strtoascii(left);
				right = strtoascii(right);
				
								
				value =left *16 + right;
			
				label[counter2][counter1] = value;
				counter1++;
			}

			counter2 ++;
		
		}
		
		bytes32 hash_hex= sha256('h');
	//	bytes32 hash2_hex= sha256('s');
		uint[32] memory  hash_value;
		string flag ='false';
		
		for(i=0;i<32;i++){
			hash_value[i]=uint(hash_hex[i]);
		}
 		

	
	
    return (hash_input,temp);
   //      return (label[0][0],label[1][0],label[counter2-1][0]);
        }
*/        


/*
  
//decode received hash values (ie, string type) into original ASCII value
    function strtoascii(uint num) returns (uint){
		if(0x30<= num && num <= 0x39){
			num = num - 0x30;
		}
		if(0x61<= num && num <= 0x66){
			num = num - 0x57;
		}
		
		return num;
    }
 */     


//Store label-id pair into index.
function storelabel(bytes32[] label, bytes32[] fid, bytes32[] ram) returns (string, bytes32){
	
	string memory label_str;
	string memory label_str2;
	uint counter = 0;  //points to which row in fid.
	
	uint where = 0;
	string memory flag = 'false';
	
//Note that here we only store the first 32 bytes of hash value in label, which are enough for
//us to have a comparison and search correct files. Thus i is incremented by 2 each time, ie, i=i+2.

	for(var i=0; i<label.length; i=i+2){
		label_str = Bytes32toString(label[i]);
		index[label_str] = fid[counter];
		randomstring[label_str] = ram[counter];
		counter ++;
		
	}
	
	
		
	//	if(stringsEqual(label_str,test)){flag = 'true';}
		
	//	fid_str = Bytes32toString(fid[0]);
		
	
	
	uint num = 0;
	label_str2  = Bytes32toString(label[num]);
	num = label.length-2;
	label_str = Bytes32toString(label[num]);
	

//	string memory test;
//	test = Bytes32toString(label[label.length-2]);
	return (label_str, randomstring[label_str]);
	 

//	return (fid);
}

function updateadd(bytes32[] labeladd, uint[] fid, bytes32[] revid) returns (uint[],uint,uint) {
    
    uint[50] memory r;
    string memory label_str;
    string memory revid_str;
    uint count = 0;
   // uint counter = 0;
   
   	string memory test = 'adf6d37ced7b66179674b1d9009a36d2';
   	
   
   	
    for (var i=0; i< labeladd.length; i=i+2){
       // var it = revidlist.find(revid[i]);
       revid_str = Bytes32toString(revid[i]);
       
       
        if (index_del[revid_str] == 0)
        {
            r[count] = 0; // set r[i] = 0
            label_str = Bytes32toString(labeladd[i]);
            index_add[label_str] = fid[count];
            //counter ++;
            
            if(count ==0){
            	uint test2 =  index_add[label_str];
            }
           
            
        }
        else
        {
            r[count] = 1;  // set r[i] = 1
            //revidlist.remove(it); // remove this revid
            index_del[revid_str] = 0;
            
        }
        count ++;
    }
    rr = r;
    
    
    uint test_fid = index_add[test];
    return (fid,test_fid,test2);
}

function read_r_value() returns (uint[50] aa) {
    
    return rr;


}


function updatedel(bytes32[] revid) returns (bool True) {
    
    string memory revid_str;
    for(var i=0; i<revid.length; i=i+2){
	//	revid_str = Bytes32toString(revid[i]);
	//   var it = revidlist.find(revid[i]);
	   revid_str = Bytes32toString(revid[i]);
	   if (index_del[revid_str] == 0)
	   {
	       //revidlist.append(revid[i]);
	       index_del[revid_str] = 1;
	      
	   }
	}
   return true;
	//	revidset.append()
	//	index[label_str] = fid[counter];
	//	counter ++;
	
}



function searchfile(string K1, string K2, uint c) returns (bytes32[50],uint) {


	
	//c is initialized from 0, this should be kept the same with the building index process in index.py.
	//uint c = 0;
//	uint re;
	//string memory c_str;
	string memory	hash_re;
	uint roundc = 0;	 
	bytes32[50] memory search_re;
	bytes32 K1_32 = stringToBytes32(K1);
	bytes32 K2_32 = stringToBytes32(K2);
	bytes32 randoms;
	//bytes32[20] memory cipher;
	//bytes32[20] memory randomm;
	//bytes20 cipher;
	string memory	tttt;
	do {
	    //c_str = uintToString(c);
		//hash_re = hashtostr32(sha256(K1,c_str));
		hash_re = hmac(K1_32, c);
		//randoms = randomstring[hash_re];
		//randoms = randomstring[hash_re];
		
		//cipher = index[hash_re];
		//cipher[c] = index[hash_re];
		//tttt = Bytes32toString(index[hash_re]);
		search_re[roundc] = hmac10(K2_32, randomstring[hash_re]) ^ ciphertobytes32(index[hash_re]);
		
		//tttt = Bytes32toString(randoms);
		c++;
		roundc++;
	}
	while(randomstring[hash_re] != 0 && roundc <=47);  // due to gas limit constraint, we choose to run only 48 rounds of search.
	search_re[roundc-1] = 0;

/*    while(index[hash_re] != 0)
    {
       c_str = uintToString(c);
       hash_re = hashtostr32(sha256(K1,c_str));
       search_re[c]=index[hash_re];
       c++; 
    }
*/
	//string memory	c_temp = uintToString(0);
	//string memory	hash_temp = hashtostr32(sha256(K1,c_temp));
 
 	//c_temp = uintToString(1);
	//string memory	hash_temp1 = hashtostr32(sha256(K1,c_temp));
	 
	

	return (search_re,c);
}

// search fucntion for the add index

function searchfile_add(string K1_add, string K_minus) returns (uint[50],uint) {


	
	//c is initialized from 0, this should be kept the same with the building index process in addindex.py.
	uint c1 = 0;
	uint re;
	//string memory c_str;
	//string memory re_str;
	string memory	hash_readd;
	string memory	revid_str1;	 
	uint[50] memory search_re;
	bytes32 K1_add32 = stringToBytes32(K1_add);
	bytes32 K_minus32 = stringToBytes32(K_minus);
	//hash_re = hmac(K1_add32, c);
	
	
//	string memory test = hmac(K1_add32,0);
	
	do {
	    hash_readd = hmac(K1_add32, c1);
	    //uint temp = index_add[hash_re];
	    //hash_re = hashtostr32(sha256(K1_add, c_str));
	    re = index_add[hash_readd];
	    revid_str1 = hmac(K_minus32, re);
	    if(index_del[revid_str1] == 0)
	    {
	    search_re[c1] = index_add[hash_readd];   
	    }
	    c1 ++;
	    //hash_re = hmac(K1_add32, c);
	    }
    while(index_add[hash_readd] != 0);

/*    while(index[hash_re] != 0)
    {
       c_str = uintToString(c);
       hash_re = hashtostr32(sha256(K1,c_str));
       search_re[c]=index[hash_re];
       c++; 
    }

	string memory	c_temp = uintToString(0);
	string memory	hash_temp = hashtostr32(sha256(K1_add,c_temp));
 
 	c_temp = uintToString(1);
	string memory	hash_temp1 = hashtostr32(sha256(K1_add,c_temp));
	 
*/	

	return (search_re,c1);
}

function getindex (string str) returns (bytes32){

	return index[str];
}


//Convert contract's hash ASCII value into string type. For example, 0xaacf12d1 ==>a a c f 1 2 d 1. 
//Here each hash value is transformed into 64 bytes in length.
/*
function hashtostr64(bytes32  hash) returns (string){
	bytes memory str = new bytes(64);
    byte left;
    byte right;
    
    
     
//    bytes32  hash  =sha256('h'); 
 
	  for(uint i=0;i<32;i++){
		  cef6f32c7919c23a6a016d49ab93daf8
		right = (hash[i]<<4) >>4;
		left = (hash[i]>>4);
		
		left=byte(asciitostring(uint(left)));
		right=byte(asciitostring(uint(right)));
		
		str[2*i] = left;
		str[2*i+1] =right;

 } 
//	return (hash,string(str));
		return (string(str));
}
 */    



//Convert contract's hash ASCII value into string type. For example, 0xaacf12d1 ==>a a c f 1 2 d 1. 
//Here each hash value is transformed into 32 bytes in length. We drop the last 32 bytes since
//the first 32 bytes are enough for us to have a comparison, and search correct file in index. 
//

function hashtostr32(bytes32  hash) returns (string){
	bytes memory str = new bytes(32);
    byte left;
    byte right;
    
    
     
//    bytes32  hash  =sha256('h'); 
 
	  for(uint i=0;i<16;i++){
		  
		right = (hash[i]<<4) >>4;
		left = (hash[i]>>4);
		
		left=byte(asciitostring(uint(left)));
		right=byte(asciitostring(uint(right)));
		
		str[2*i] = left;
		str[2*i+1] =right;

 } 
//	return (hash,string(str));
		return (string(str));
}


 
 
 
//decode contract's hash ASCII value into string type
    function asciitostring(uint num) returns (uint){
		if(0x00<= num && num <= 0x09){
			num = num + 0x30;
		}
		if(0x0a<= num && num <= 0x0f){
			num = num + 0x57;
		}
		
		return num;
    }
 
 
 
 //Transform uint-type into string-type. The uint-type input should not be larger than 999. Since the search result only consists of about 300 files generally.
  function uintToString(uint value) constant returns (string) {
 	bytes32 ret; 
 	uint v = value; 
 	bytes memory ret_str;
    if (v == 0) {
        ret = '0';
    }
    else { 
        while (v > 0) {
            ret = bytes32(uint(ret) / (2 ** 8));
            ret |= bytes32(((v % 10) + 48) * 2 ** (8 * 31));
            v /= 10;
        }
    }
    
    if(value>= 0 && value<=9 ){ 
    	ret_str = new bytes(1);
    	ret_str[0] = ret[0];
    	
    }
    if(value >= 10 && value <= 99){
    	ret_str = new bytes(2);
    	
    	ret_str[0] = ret[0];
    	ret_str[1] = ret[1];
    }
    if(value >= 100 && value <= 999){
    	ret_str = new bytes(3);
    	ret_str[0] = ret[0];
    	ret_str[1] = ret[1];
    	ret_str[2] = ret[2];
    }
    
    
    return string(ret_str);
}        
 
    
        
        
	function Bytes32toString(bytes32 input)   returns (string){ 
		bytes memory bytesString = new bytes(32);
		
		for (uint i=0;i<32;i++){
			bytesString[i] = input[i];  //transform string into bytes array
		}
		
		return string(bytesString);		//transform bytes array into string

	}
/*	
	function Bytes20toString(bytes20 input)   returns (string){ 
		bytes memory bytesString = new bytes(20);
		
		for (uint i=0;i<20;i++){
			bytesString[i] = input[i];  //transform string into bytes array
		}
		
		return string(bytesString);		//transform bytes array into string

	}
*/	
	
	function stringsEqual(string memory _a, string memory _b) internal returns (bool) {
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

    function hmac(bytes32 key, uint c) returns (string digest){
        //bytes32 memory key32 = key
        string memory c_str = uintToString(c);
        bytes32 in32 = key ^ ipad;
        string memory in32_str = Bytes32toString(in32);
        bytes32 result = sha256(in32_str, c_str);
        //string memory result_str = hashtostr32(result);
        bytes32 out32 = key ^ opad;
        string memory out32_str = Bytes32toString(out32);
        bytes32 resultc = sha256(out32, result);
        return hashtostr32(resultc);
}   
   function hmac10(bytes32 key, bytes32 ram) returns (bytes32 digest){
        //bytes32 memory key32 = key
        //string memory c_str = uintToString(c);
        //bytes20 outputre;
        //bytes32 outputre = 0x0000000000000000000000000000000000000000000000000000000000000000;
        //byte rrr;
        string memory ram_str = Bytes32toString(ram);
        bytes32 in32 = key ^ ipad;
        string memory in32_str = Bytes32toString(in32);
        bytes32 result = sha256(in32_str, ram);
        //string memory result_str = hashtostr32(result);
        bytes32 out32 = key ^ opad;
        string memory out32_str = Bytes32toString(out32);
        bytes32 resultc = sha256(out32, result);
        //for (uint i=19;i>=0;i--){
		//	rrr = resultc[i];
		//	outputre = outputre | rrr;
		//	outputre = outputre >>8;
		//	
			  //transform into bytes20 array
		//}
        return resultc;
}

/*
 function Bytes32toString(bytes32 input)   returns (string){ 
		bytes memory bytesString = new bytes(32);
		
    for (uint j=0; j<32; j++) {
        byte char = byte(bytes32(uint(input) * 2 ** (8 * j)));
        if (char != 0) {
            bytesString[j] = char;
        }
	}
	
	return string(bytesString);
    }
*/ 


   function stringtobyte(uint t) returns (uint){
        if(0x30<= t && t <= 0x39){
            t = t - 0x30;
        }
        if(0x61<= t && t <= 0x66){
            t = t - 0x57;
        }
        return t;
    }
   function stringToBytes32(string memory source) returns (bytes32) {
    //string memory source = "029238f56f3af43959ce4a51d7b5c7ab7595fe0b48fc4c99ec59a1bd2281f606";
    //bytes memory ss = bytes(source);
    //assembly {
    //    result := mload(byte(33,source))
    //}
    bytes32 result = 0x0000000000000000000000000000000000000000000000000000000000000000;
    bytes memory ss = new bytes(2);
    bytes memory resultc = bytes(source);
    uint resleft;
    uint resright;
    //uint out;
    byte output;
    for (uint i = 63; i > 1; i=i-2 ){
        ss[0] = resultc[i-1];
        ss[1] = resultc[i];
        resleft = stringtobyte(uint(ss[0])) <<4 ;
        resright = stringtobyte(uint(ss[1]));
        //out = resleft | resright;
        output = byte(resleft | resright);
        result =  result | output;

        result = result >>8;

        //result =  result | output;
        
    }
    ss[0] = resultc[0];
    ss[1] = resultc[1];
    resleft = stringtobyte(uint(ss[0])) <<4 ;
    resright = stringtobyte(uint(ss[1]));
    //out = resleft | resright;
    output = byte(resleft | resright);
    result =  result | output;
    //result = result | output;
    /*
    bytes memory ss = new bytes(2);
    //uint[] memory res = new  uint[2];
    uint resleft;
    uint resright;
    uint out;
    byte output;
    bytes32 result = 0x0000000000000000000000000000000000000000000000000000000000000000;
    //bytes memory res1 = new  bytes(32);
    
    //bytes2 you = 0x3333;
    //you = you << 4;
    
    ss[0] = resultc[2];
    ss[1] = resultc[3];
    
    resleft = stringtobyte(uint(ss[0])) <<4 ;
    resright = stringtobyte(uint(ss[1]));
    out = resleft | resright;
    output = byte(out);
    result =  result | output;
    result = result >>8;
    result =  result | output;
    //result[0] = output;
    
    //res = res <<4;
    //output = bytes2(res);
    //output[0] = res[1];
    //res1 = res<<4;
    //res[1] = stringtobyte(uint(ss[1]));
    //res[0] = bytes(q);
    */
    return result;
    
    
}
   function ciphertobytes32 (bytes32 inc) returns (bytes32)
   {
     //bytes32 inc = 0x3239386661623836323131353733333031663932316238323238353364353466;  
     bytes32 result = 0x0000000000000000000000000000000000000000000000000000000000000000;
     bytes memory ss = new bytes(2);
     //ss[0] = inc[30];
    // ss[1] = inc[31];
     uint resleft;
     uint resright;
     byte output;
     for (var i = 31; i >1 ; i=i-2) {
        ss[0] = inc[i-1];
        ss[1] = inc[i];
        resleft = stringtobyte(uint(ss[0])) <<4 ;
        resright = stringtobyte(uint(ss[1]));
        //out = resleft | resright;
        output = byte(resleft | resright);
        result =  result | output;

        result = result >>8; 
     }
     ss[0] = inc[0];
     ss[1] = inc[1];
     resleft = stringtobyte(uint(ss[0])) <<4 ;
     resright = stringtobyte(uint(ss[1]));
     //out = resleft | resright;
     output = byte(resleft | resright);
     result =  result | output;
     return result;
       
   }
}
 





