//var ConvertLib = artifacts.require("./ConvertLib.sol");
//var MetaCoin = artifacts.require("./MetaCoin.sol");
var MyContract = artifacts.require("./MyContract.sol")

module.exports = function(deployer) {
//  deployer.deploy(ConvertLib);
//  deployer.link(ConvertLib, MetaCoin);
// deployer.deploy(MetaCoin);
	deployer.deploy(MyContract);
};
