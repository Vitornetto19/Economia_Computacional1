# inserindo n registros com uma tupla de dados

# 04_create_data_nrecords.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# criando uma lista de dados

lista = [(
    'Fabio', 23, '44455566678', 'fabio@email.com', '1234-5678', 'Belo horizonte', 'MG', '2014-06-09'),
    ('joao', 55, '57829786756', 'joao@email.com', '11-1234-4321', 'Sao paulo', 'SP', '2014-06-09'),
    ('Xavier', 24, '66688899967', 'xavier@email.com', '12-3456-7654', 'Campinas', 'SP', '2014-07-08')]
    
# inserindo dados na tabela

cursor.executemany("""
INSERT INTO clientes(nome,idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)

conn.commit()


print('Dados inseridos com sucesso')

conn.close()


