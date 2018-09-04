var MyContract = artifacts.require("./MyContract.sol");
var crypto = require('crypto');

//var label = new Array()   //store all the label.
//var fid = new Array() 	//store all the corresponding file id.
var revid = new Array() // store all the corresponding revids. ****
//var label_part = new Array() //store the labels that should be uploaded at one time.
//var fid_part = new Array() //store the file id that should be upleader at one time.
var revid_part = new Array()  //store the revids that should be upleader at one time. ****
//var label_last = new Array() //store the labels that are less than number of step and will be uploaded at last.
//var fid_last = new Array() //store the file id that are less than number of step and will be uploaded at last.
var revid_last = new Array() //store the revids that are less than number of step and will be uploaded at last. ****

var hash;
var hashbuf;
var total;

function read_json(){

delindex = require("./buildIndex/db/labeldel.json");  //******
//console.log(addindex);
var i=0;


//read json data of addindex
for(var term in delindex){  //******

//	if(i<100){
	//label[i] = addindex[i][0];
	//fid[i] = addindex[i][1];
	revid[i] = delindex[i];   //******

	i++;
//	}
}
//console.log(fid);
total = i;


//Since contract only read the same number of elements with input array, and for each element in iuput array,
//contract will store with twice the size. This results in that contract only read half content of the input
//array. Thus we store another half of empty content in the input array.
//Now this step has been moved to the subsequent while loop.


/*
for(var j=i; j< 2*i;j++){
	label[j]= 'empty';
//	fid[j] = 'empty';
}

	console.log(label);
//	console.log(fid);
*/


}


module.exports = function (callback){
	var instance;
	
	MyContract.deployed().then(function(inst){
	instance = inst;

	read_json();
	
//	console.log(instance.address);


 //	return instance.storelabel(label,fid);
}).then(function(){
	
	console.log('this is total number for label.');
	console.log(total);
	var step = 50;
	var j = 0;
	var k = 0;
	var counter = 0;
	
	
	
	
	while(total > step){
	
	//label_part[counter] = new Array();
	//fid_part[counter] = new Array();
	revid_part[counter] = new Array();  //******
	
	for(j=0; j<step; j++){
			//label_part[counter][j] = label[counter*step + j];
			revid_part[counter][j] = revid[counter*step + j];
			//fid_part[counter][j] = fid[counter*step + j];  //******
	
	}
	
	for(j=0; j<step; j++){
			//label_part[counter][step+j] = 'empty';
			revid_part[counter][step+j] = 'empty';  //******
		}
	
	instance.updatedel(revid_part[counter]).then(function(read_re){
			console.log(read_re);
			console.log('Revids Store Successfully');
		}).catch(function (err){
			console.log(err);
		})
	
	//console.log(label_part); 
	total = total - step;
	counter ++;
	
	}
	
	//store last labels and revids the number of which is less than step.
	for(j=0;j<total;j++){
		
		//label_last[j] = label[counter*step + j];
		//fid_last[j] = fid[counter*step + j];
		revid_last[j] = revid[counter*step + j];	
	}	
	
	//if fid is stored using uint type, then size of label and revid should be twice as fid.
	for(k=j; k< 2*j; k++){
		//label_last[k] = 'empty';
		revid_last[k] = 'empty';
	}
	
	//console.log(label_part); 
	
	}).catch(function (err){
			console.log(err);
	})
};


//The following commented out code are wrong because promise is asynchronous, the codes in 'then()' will not
//be executed immediately and the 'for' loop will continue to proceed. This result in that the parameters in 
//'then()' will be updated after each loop. Thus we need to use different representations for parameters in 
//'then()', eg, using 'label_part[counter]' instead of 'label'.
/*
	while(total > step){
		
		
	
		for(j=0; j<step; j++){
			label_part[j] = label[counter*step + j];
			fid_part[j] = fid[counter*step + j];
		}
		
		//if fid is stored using uint type, then size of label should be twice as fid.
		for(j=0; j<step; j++){
			label_part[step+j] = 'empty';
		}
		
		total = total - step;
		counter ++;
		
		console.log(label_part);
		
		
		instance.storelabel(label_part,fid_part).then(function(read_re){
			console.log(read_re);
			console.log('Store Successfully');
		}).catch(function (err){
			console.log(err);
		})
	}
	
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
