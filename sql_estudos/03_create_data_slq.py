# 03_create_data_sql.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserindo dados na tabela

cursor.execute("""
INSERT INTO clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em)
VALUES ('REGIS',35, '45666778998','regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Amanda', 23, '12323434567', 'amand@email.com', '23-34567-7899', 'Rio de janeiro', 'RJ', '2017-09-07')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Jose', 33, '56788897645', 'jose@email.com', '51-97878-5645', 'Rio grande do sul', 'RS','2020=09-09')
""")

# gravando no bd
conn.commit()


print("dados inseridos com sucesso")

conn.close()



