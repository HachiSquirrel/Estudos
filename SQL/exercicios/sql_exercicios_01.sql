-- E1 Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

select *
from livro 
where publicacao > '2014-12-31'
order by cod 

-- E2 Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

select titulo, valor
from livro 
order by valor desc
limit 10

-- E3  Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente

 select count(l.titulo) as quantidade, ed.nome , en.estado , en.cidade
from livro l
inner join editora ed
on l.editora = ed.codeditora 
inner join endereco en
on ed.endereco = en.codendereco
group by ed.codeditora 
order by quantidade desc
limit 5
-- E4 Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select au.nome, au.codautor , au.nascimento, count(l.autor) as quantidade
from livro l
full join autor au
on l.autor = au.codautor
group by l.autor , au.nascimento , au.nome
order by nome

-- E5 Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno

select a.nome
from autor a
inner join livro l
on a.codautor = l.autor
inner join editora ed
on l.editora = ed.codeditora
inner join endereco en
on en.codendereco = ed.endereco
where en.estado not in ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
group by a.nome
order by a.nome

-- E6 Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select a.codautor, a.nome, count(l.publicacao) as quantidade_publicacoes
from livro l full join autor a
on l.autor = a.codautor
group by a.nome
order by quantidade_publicacoes desc
limit 1

-- E7 Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select a.nome
from autor a 
full join livro l
on l.autor = a.codautor
where l.publicacao ISNULL
group by a.nome
order by a.nome

--E8 Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd

with tabela_02 as (
select 
 vendedor.cdvdd,
 vendedor.nmvdd, 
 count(vendas.qtd) as qtd_vendas
from tbvendedor vendedor
join tbvendas vendas
on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.nmvdd
)

select cdvdd, 
       nmvdd
from tabela_02
where qtd_vendas = (select max(qtd_vendas) from tabela_02)

-- E9 Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro

select t.cdpro as cdpro, t.nmpro as nmpro
from tbvendas t 
where status = "Concluído" and t.dtven BETWEEN "2014-02-03" and "2018-02-02"
group by t.cdpro
order by count(t.cdpro) desc
limit 1

-- E10 A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decima

select tbvendedor.nmvdd as vendedor, sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas, ROUND((sum(tbvendas.vrunt * tbvendas.qtd)*perccomissao) /100, 2) as comissao
from tbvendas
inner join tbvendedor
on tbvendas.cdvdd = tbvendedor.cdvdd
where status = 'Concluído'
group by tbvendas.cdvdd
order by comissao desc

-- E11 Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.


with tb_soma_concluida as (
select cdcli, nmcli, sum(qtd * vrunt) as gasto
from tbvendas t
where status = 'Concluído'
group by nmcli
)

select cdcli, nmcli, gasto
from tb_soma_concluida
where gasto = (select max(gasto) from tb_soma_concluida)


-- E12 Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


--Observação: Apenas vendas com status concluído


with tb_valor_total_bruto as (

Select dep.cddep, dep.nmdep, dep.dtnasc, sum(vendas.qtd * vendas.vrunt) as valor_total_vendas
from tbdependente dep
inner join tbvendedor vendedor 
on dep.cdvdd = vendedor.cdvdd 
inner join tbvendas vendas 
on vendedor.cdvdd = vendas.cdvdd 
where status = 'Concluído'
group by dep.cddep 
having valor_total_vendas <> 0
)

Select cddep, nmdep, dtnasc, valor_total_vendas
from tb_valor_total_bruto
where valor_total_vendas = (select min(valor_total_vendas) from tb_valor_total_bruto)

-- E13 Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

Select 
	cdpro,
	nmcanalvendas, 
	nmpro, 
	sum(qtd) as quantidade_vendas
from tbvendas t 
where status = 'Concluído'
group by cdpro, nmcanalvendas 
order by quantidade_vendas
limit 10

--E14 Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

--Observação: Apenas vendas com status concluído.

Select 
	estado,
	round(avg(qtd * vrunt),2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado 
order by gastomedio desc

--E15 Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

select cdven 
from tbvendas t 
where deletado = 1
order by cdven 

--E16 Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

--Obs: Somente vendas concluídas.

Select 
	estado,
	nmpro,
	round(avg(qtd), 4) as quantidade_media 
from tbvendas
where status = 'Concluído'
group by estado , nmpro
order by estado, nmpro