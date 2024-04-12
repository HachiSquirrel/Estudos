CREATE VIEW fact_Locacao as
	SELECT l.idLocacao,
		l.idCliente,
		l.idCarro,
		l.idVendedor,
		l.idCombustivel,
		l.qtdDiaria,
		date(substr(l.dataLocacao, 1, 4) || '-' || substr(l.datalocacao, 5, 2) || '-' || substr(l.dataLocacao, 7, 2)) AS dataLocacao,
		l.horaLocacao,
		date(substr(l.dataEntrega, 1, 4) || '-' || substr(l.dataEntrega, 5, 2) || '-' || substr(l.dataEntrega, 7, 2)) AS dataEntrega,
		l.horaEntrega
	FROM Locacao l
		JOIN Cliente c ON l.idCliente = c.idCliente
		JOIN Carros ca ON l.idCarro = ca.idCarro
		JOIN Vendedor v ON l.idVendedor = v.idVendedor
		JOIN Combustivel co ON l.idCombustivel = co.idCombustivel;


CREATE VIEW dim_Cliente
AS
	SELECT idCliente,
		nomeCliente,
		cidadeCliente,
		estadoCliente,
		paisCliente
	FROM Cliente c;

CREATE VIEW dim_Carros
AS
	SELECT idCarro,
		kmCarro,
		classiCarro,
		marcaCarro,
		modeloCarro,
		anoCarro
	FROM Carros ca;


CREATE VIEW dim_Vendedor
AS
	SELECT idVendedor,
		nomevendedor,
		sexoVendedor,
		estadoVendedor
	FROM Vendedor v;

CREATE VIEW dim_Combustivel
AS
	SELECT idCombustivel,
		tipoCombustivel
	FROM Combustivel co;
	