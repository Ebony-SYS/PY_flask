CREATE TABLE IF NOT EXISTS tb_produtos(
    id BIGINT AUTO_INCREMENT,
    codigo INT(4) UNSIGNED ZEROFILL NOT NULL,
    nome VARCHAR(60), 
    qtd_est NOT NULL,
    preco FLOAT,
    fk_categoria BIGINT,

    PRIMARY KEY('id')
    FOREIGN KEY('fk_categoria') REFERENCES tb_categorias('id')
)

CREATE TABLE IF NOT EXISTS tb_categorias(
    id BIGINT AUTO_INCREMENT,
    nome VARCHAR(40), 
    descricao VARCHAR(255) NOT NULL, 

    PRIMARY KEY('id')    
)

