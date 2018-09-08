var MyContract = artifacts.require("./MyContract.sol");
MyContract.synchronization_timeout = 0;

var crypto = require('crypto');

var label = new Array()   //store all the label.
var fid = new Array() 	//store all the corresponding file id.
var ram = new Array() // store all the random strings ****
var label_part = new Array() //store the labels that should be uploaded at one time.
var fid_part = new Array() //store the file id that should be upleader at one time.
var ram_part = new Array() // store all the random strings ****
//var label_part2 = new Array() //store the labels that should be uploaded at one time.
//var fid_part2 = new Array() //store the file id that should be upleader at one time.
//var ram_part2 = new Array() // store all the random strings ****
var label_last = new Array() //store the labels that are less than number of step and will be uploaded at last.
var fid_last = new Array() //store the file id that are less than number of step and will be uploaded at last.
var ram_last = new Array() // store all the random strings ****

var hash;
var hashbuf;
var total;

function read_json(){

index = require("./buildIndex/db/labelfinance10.json");
//index = require("./local/db/labeltest2.json");
//string = require("./local/db/randomstring.json");

//console.log(index)
var i=0;


//read json data of index
for(var term in index){

//	if(i<100){
    if (term != null) {
    
    label[i] = index[i][0];
    fid[i] = index [i][1];
    ram[i] = index [i][2];
    i++;
    
    }
    
	//label[i] = index[i][0];
	//fid[i] = index[term];
	//ram[i] = string[i];
	//i++;
//	}
}

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
	
	//step defines how much data are stored at once.
	var step =70;
	var j =0;
	var k = 0;
	var counter = 0;


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


    
	while(total > step){
		
		label_part[counter] = new Array();
		fid_part[counter] = new Array();
		ram_part[counter] = new Array();
		//label_part2[counter] = new Array();
		//fid_part2[counter] = new Array();
		//ram_part2[counter] = new Array();
		
		for(j=0; j<step; j++){
			label_part[counter][j] = label[counter*step + j];
			fid_part[counter][j] = fid[counter*step + j];
			ram_part[counter][j] = ram[counter*step + j];
			//label_part2[counter][j] = label[counter*step + j +50];
			//fid_part2[counter][j] = fid[counter*step + j +50];
			//ram_part2[counter][j] = ram[counter*step + j+50];
			 
		}
		
		//if fid is stored using uint type, then size of label should be twice as fid.
		for(j=0; j<step; j++){
			label_part[counter][step+j] = 'empty';
			//label_part2[counter][step+j] = 'empty';
		}
		
//		console.log(label_part[counter]);
		
		
		
	
		
		instance.storelabel(label_part[counter],fid_part[counter],ram_part[counter]).then(function(read_re){
			console.log(read_re);
			console.log('Store Successfully');
		}).catch(function (err){
			console.log(err);
		})
		/*instance.storelabel(label_part2[counter],fid_part2[counter],ram_part2[counter]).then(function(read_re){
			console.log(read_re);
			console.log('Store Successfully');
		}).catch(function (err){
			console.log(err);
		})*/
		
		
		total = total -step;
		counter +=1;

	}
	





	
	//store last labels the number of which is less than step.
	for(j=0;j<total;j++){
		
		label_last[j] = label[counter*step + j];
		fid_last[j] = fid[counter*step + j];
		ram_last[j] = ram[counter*step + j];	
	}	
	
	//if fid is stored using uint type, then size of label should be twice as fid.
	for(k=j; k< 2*j; k++){
		label_last[k] = 'empty';
	}
		
	

	
 	instance.storelabel(label_last,fid_last, ram_last).then(function(read_re){
		console.log(read_re);
		console.log('Store Successfully');
	}).catch(function (err){
		console.log(err);
	})



}).catch(function (err){
	console.log(err);
})
	
};






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
