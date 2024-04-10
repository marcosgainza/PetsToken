const PetsToken = artifacts.require("PetsToken");

module.exports = function(deployer, network, accounts) {
  // Suponiendo que el constructor de PetsToken espera 4 parámetros
  const param1 = "my token"; // Define el valor para param1
  const param2 = "mt"; // Define el valor para param2
  const param3 = 1000000; // Define el valor para param3
  const param4 = accounts[0]; // Usa la primera cuenta en la red de prueba

  deployer.deploy(PetsToken, param1, param2, param3, param4);
};
