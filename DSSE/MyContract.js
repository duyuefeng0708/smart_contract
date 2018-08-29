//This code has been no used, and can be regarded as test code.



/*
var MyContract = artifacts.require("./MyContract.sol");
var crypto = require('crypto');

var label = new Array()   //store all the label.
var fid = new Array() 	//store all the corresponding file id.
var label_part = new Array() //store the labels that should be uploaded at one time.
var fid_part = new Array() //store the file id that should be upleader at one time.
var label_last = new Array() //store the labels that are less than number of step and will be uploaded at last.
var fid_last = new Array() //store the file id that are less than number of step and will be uploaded at last.

var hash;
var hashbuf;
var total;

function read_json(){

index = require("./local/db/label.json");

//console.log(index);

var i=0;


//read json data of index
for(var term in index){
//	if(i<100){
	label[i] = term;
	fid[i] = index[term];
	i++;
//	}
}

total = i;

//Since contract only read the same number of elements with input array, and for each element in iuput array,
//contract will store with twice the size. This results in that contract only read half content of the input
//array. Thus we store another half of empty content in the input array.



for(var j=i; j< 2*i;j++){
	label[j]= 'empty';
//	fid[j] = 'empty';
}
	console.log(i);
	console.log(label);
//	console.log(fid);




}


module.exports = function (callback){
	var instance;
	
	MyContract.deployed().then(function(inst){
	instance = inst;

	read_json();
	
	console.log(instance.address);
	

//	return instance.searchfile.call(K1);




 //	return instance.storelabel(label,fid);
}).then(function(){

	console.log(total);
	
	//step defines how much data are stored at once.
	var step =100;
	var j =0;
	var counter = 0;
	
	while(total > step){
		
		
		for(j=0; j<step; j++){
			label_part[j] = label[counter*step + j];
			fid_part[j] = fid[counter*step + j];
		}
		for(j=0; j<step; j++){
			label_part[step+j] = 'empty';
		}
		
		total = total - step;
		counter ++;
		
		instance.storelabel(label_part,fid_part).then(function(read_re){
			console.log('Store Successfully');
		}).catch(function (err){
			console.log(err);
		})
	}
	
	
	//store last labels the number of which is less than step.
	for(j=0;j<total;j++){
		label_last[j] = label[counter*step + j];
		fid_last[j] = fid[counter*step + j];	
	}
	
		instance.storelabel(label_part,fid_part).then(function(read_re){
		console.log('Store Successfully');
	}).catch(function (err){
		console.log(err);
	})



}).catch(function (err){
	console.log(err);
})
	



};


/*
module.exports = function (callback){
	var instance;
	MyContract.deployed().then(function(inst){
	instance = inst;

	read_json();
	
	console.log(instance.address);
	//for(var i in label){
		instance.set.call(label[1],1);
	//}
}).then(function(read_re){
	console.log(read_re);
}).catch(function (err){
	console.log(err);
})
};

*/



/*
function read_json(){
	//var hashbuf;
	var hashobj = crypto.createHash('sha256');
	
	hashobj.update(data);
	hashbuf = hashobj.digest();
	console.log(hashbuf);
	console.log(hashbuf[0]);
//	hash=Array.prototype.slice.call(hashbuf, 0);
	

	hash = hashbuf.toString('hex');
	 
	console.log(hash);
	var temp;
	for(var i=0; i<32; i++){
	console.log(hashbuf[i]);
		temp += hashbuf[i];
	}
//	console.log(label);
	console.log(temp);
	6d93ac6b9db975b1b26e1839e4909746f83915c1c2dc71109cb6f6ad53d82238
}
*/



//function callback(){
//	console.log("this is callback");
//	alert("I am here");
//}
