// SPDX-License-Identifier: MIT
// Contrato inteligente PetsToken que implementa ERC-721
// Adaptado para permitir transferencias y acceso continuo

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Declara el contrato PetsToken
contract PetsToken is ERC721Enumerable, Ownable {
    // Declara variables de estado
    string private _baseTokenURI;

    // Contador para asignar IDs únicos a las mascotas
    uint256 private nextTokenId;

    // Mapeo de ID de token a información de mascota
    mapping(uint256 => Mascota) private mascotas;

    // Evento emitido cuando se tokeniza una nueva mascota
    event MascotaTokenizada(uint256 tokenId, string nombre);

    // Estructura para almacenar información de la mascota
    struct Mascota {
        string nombre;
        string raza;
        string color;
        string historiaClinica;
        string foto;
    }

    // Declara el constructor
    constructor(string memory name, string memory symbol, string memory baseTokenURI, address initialOwner) ERC721(name, symbol) Ownable(initialOwner) {
        _baseTokenURI = baseTokenURI;
    }

    // Función para tokenizar una nueva mascota
    function tokenizarMascota(
        string memory _nombre,
        string memory _raza,
        string memory _color,
        string memory _historiaClinica,
        string memory _foto
    ) external onlyOwner {
        uint256 tokenId = nextTokenId;
        mascotas[tokenId] = Mascota(_nombre, _raza, _color, _historiaClinica, _foto);
        _mint(owner(), tokenId);
        nextTokenId++;

        emit MascotaTokenizada(tokenId, _nombre);
    }

    // Función para transferir una mascota a otro dueño
    function transferirMascota(address _nuevoDueno, uint256 _tokenId) external onlyOwner {
        // Asegura que el dueño actual sea el propietario original del token
        require(ownerOf(_tokenId) == owner(), "No eres el dueno original de la mascota");
        
        // Transfiere el token al nuevo dueno
        _safeTransfer(owner(), _nuevoDueno, _tokenId);
    }

    // Función para obtener información de una mascota por su ID de token
    function obtenerInformacionMascota(uint256 _tokenId) external view returns (Mascota memory) {
        return mascotas[_tokenId];
    }

    // Función para obtener el URI base de los tokens
    function getBaseTokenURI() external view returns (string memory) {
        return _baseTokenURI;
    }
}
