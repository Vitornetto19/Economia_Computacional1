# Lendo as informacoes do banco de dados -> comando PRAGMA
# listar tabelas -> SELECT name FROM sqlite_master...
# ler schema da tabela -> SELECT sql FROM sqlite_master

# 10_view_table_info.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
nome_tabela = 'clientes'

# obtendo informacoes da tabela

cursor.execute ('PRAGMA tabela_info({})'.format(nome_tabela))

colunas = [tuplas[1] for tupla in cursor.fetchall()]
print('Colunas:', colunas)
#ou
# for coluna in colunas:
#    print(coluna)

# listando as tabelas do db
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))
    
# obtebdo o schema da tabela

cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema')
for schema in cursor.fetchall():
    print("%s" % (schema))
    
conn.close()



