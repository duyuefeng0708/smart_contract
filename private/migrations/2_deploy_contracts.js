//var ConvertLib = artifacts.require("./ConvertLib.sol");
//var MetaCoin = artifacts.require("./MetaCoin.sol");
var MyContract = artifacts.require("./MyContract.sol");
MyContract.synchronization_timeout = 0;
module.exports = function(deployer) {
	deployer.deploy(MyContract);
};
