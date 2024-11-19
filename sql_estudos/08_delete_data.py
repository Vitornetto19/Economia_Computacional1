# Delete - deletando os dados

# 08_delete_data.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 2

# excluindo um registro da tabela

cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print("Registro deletado com sucesso")

conn.close()

