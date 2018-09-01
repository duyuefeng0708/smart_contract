var MyContract = artifacts.require("./MyContract.sol");


MyContract.deployed().then(function(instance){
	console.log(instance);
});
