var MyContract = artifacts.require("./MyContract.sol");


var searchtoken = require("./buildIndex/db/searchtokenadd.json");

//var index = require("./local/db/labeladd.json");


module.exports = function (callback){
	var instance;
	MyContract.deployed().then(function(inst){
	instance = inst;
	
	

	var label = new Array();
	var fid = new Array();
	
	var total=0;


	//for(var term in index){


	//label[total] = term.substring(0,32);
	
	//fid[total] = index[term];
	
	//total++;

	//}  

	

//	console.log(fid)

//	console.log(searchtoken);
	
//	console.log(instance.address);
	
	var K1 = searchtoken[0];
	var K_minus = searchtoken[1];
	//console.log (K1, K_minus)	


//	console.log(label[total-1]); 
	
	
//The following commented out codes can be used to get all the data in 'index' that are stored in contract.
//We have checked that the data in 'index' stored in contract are consistent with that stored locally.
/*
	var i=0;
	var j=0;
	var flag = 'true';
	for(i=0; i<total; i++){
		
 		
		instance.getindex.call(label[i]).then(function(re){

			if(re != fid[j]){flag = 'flase';}
			console.log(re);
			console.log(fid[j]);
		//	console.log(j);
			j++;
			console.log(flag);
		});
	
	}
*/

//	var key = "cef6f32c7919c23a6a016d49ab93daf8";
//	return instance.getindex.call(key);

//1c9e3f2f5e6f2985a5abcde72b75b97c
	
//	return	instance.getindex.call(label[total-1]);
//	console.log(K1);
	return	instance.searchfile_add.call(K1, K_minus);
}).then(function(read_re){
	console.log(read_re);
}).catch(function (err){
	console.log(err);
})
};


