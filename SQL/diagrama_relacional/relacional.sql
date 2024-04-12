CREATE TABLE IF NOT EXISTS Locacao (
	idLocacao INT PRIMARY KEY,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	idCombustivel INT,
	dataLocacao DATETIME,
	horaLocacao TIME,
	qtdDiaria INT,
	dataEntrega DATE,
	horaEntrega TIME,
	FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
	FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
	);

INSERT OR IGNORE INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, idCombustivel, dataLocacao, horaLocacao, qtdDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, idCombustivel, dataLocacao, horaLocacao, qtdDiaria, dataEntrega, horaEntrega
FROM tb_locacao;

select * from Locacao;

------------------------------

CREATE TABLE IF NOT EXISTS Carros (
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	classiCarro VARCHAR(100),
	marcaCarro VARCHAR(100),
	modeloCarro VARCHAR(100),
	anoCarro INT
	);



INSERT OR IGNORE INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;
----------------------------------

CREATE TABLE IF NOT EXISTS Cliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR (100),
	cidadeCliente VARCHAR(100),
	estadoCliente VARCHAR(100),
	paisCliente VARCHAR(100)
	);


INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT (idCliente), nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

SELECT * FROM Cliente 

---------------------------------

CREATE TABLE IF NOT EXISTS Vendedor (
	idVendedor INT PRIMARY KEY,
	nomevendedor VARCHAR(100),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(100)
	);

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT (idVendedor), nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

SELECT * FROM Cliente 

---------------------------------

CREATE TABLE Combustivel (
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(100)
	);

INSERT OR IGNORE INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao;

SELECT * FROM Combustivel;

