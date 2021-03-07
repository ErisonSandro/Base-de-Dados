"""
CRIANDO BD NA MÃO COM PYTHON
"""

import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Nene', 70))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Toca', 'peso': 50})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'luna', 'peso': 15})
# conexao.commit()

# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 12})
#conexao.commit()

#cursor.execute('SELECT * FROM clientes')
#cursor.execute('SELECT nome, peso FROM clientes WHERE peso >= :peso', {'peso': 50})
#cursor.execute('SELECT nome FROM clientes WHERE nome = :nome', {'nome': 'Nene'})

for linha in cursor.fetchall():
    #identificador, nome, peso = linha
    #print(identificador, nome, peso)

    nome, peso = linha
    print(nome, peso)


cursor.close()
conexao.close()
