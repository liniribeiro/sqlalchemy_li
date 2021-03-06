[![Build Status](https://travis-ci.org/aliniribeiroo/sqlalchemy_li.svg?branch=master)](https://travis-ci.org/aliniribeiroo/sqlalchemy_li)

Projeto criado para armazenar estudos realizados com SQLAlchemy.



Criando e entendendo a Engine


Engine é como o sqlAlchemy se comunica com o banco de dados, então, quando criamos uma engine,
precisamos adicionar a URL do banco de dados que iremos utilizar.
Então, conseguimos acessar o banco de dados, a partir de comandos da engine.

Podemos executar comandos direto da engine:  engine.execute(...)
Temos também a opção de criar uma conexão com o banco:
Exemplo:
trans = conn.begin()
conn.execute('INSERT INTO "EX1" (name)'
             'VALUES ("Hello")')
trans.commit()


#Criando e entendendo as Sessions


O que faz o SQLAlchemy tão atrativo, é o seu ORM. O ORM precisa ter uma session que faz o meio de campo entre os objetos que iremos trabalhar e a engine que se comunica com o banco de dados.
Para isso, precisamos utilizar uma função chamada sessionmaker e passar a engine para ela.


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

Vamos utilizar as sessions para conversar com as tabelas e realizar nossas queries, mas quem de fato executa estes comandos na tabela, é a nossa engine.



#Criando tabelas

Para criar uma tabela, criamos uma classe que contém atributos. Cada classe será uma tabela em nosso banco de dados e cada atributo, será uma coluna da tabela.
Para mapear qual tabela será vinculada a qual classe em nossos arquivos, vamos utilizar o Declarativemodel do SQLALchemy.

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




Alembic:
É uma leve ferramenta de migração de banco de dados, para ser utilizada com o SQLAlchemy para Python.
https://alembic.sqlalchemy.org/en/latest/



Factory-boy: 
https://factoryboy.readthedocs.io/en/latest/
https://medium.com/@vittorio.camisa/agile-database-integration-tests-with-python-sqlalchemy-and-factory-boy-6824e8fe33a1


Comands:
Pipenv criar requirements: pipenv lock -r > requirements.txt
pipenv lock -r requirements.txt



Alembic

Criar revision:  alembic revision --autogenerate -m "Added account table"
Aplicar revision: alembic upgrade head
















































Tutorial seguido: https://leportella.com/sqlalchemy-tutorial.html