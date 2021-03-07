import pymysql.cursors
from contextlib import contextmanager

# CRUD = CREATE / READ / UPDATE / DELETE

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()

# ADICIONANDO UM UNICO VALOR
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#         '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Toca', 112, 220))
#         conexao.commit()

#ADICIONANDO VARIAS PESSOAS COM LISTA
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#         '(%s, %s, %s, %s)'
#
#         dado = [
#             ('Muriel', 'Figueiredo', 19, 55),
#             ('MARIAZINHA', 'DA SILVA', 50, 35),
#             ('ROGER', 'CARVALHO', 35, 28),
#             ('MEUSA', 'XUARA', 65, 40)
#         ]
#
#         cursor.executemany(sql, dado)
#         conexao.commit()


#APAGANDO UM UNICO ID COM WHERE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (10, ))
#         conexao.commit()

# APAGANDO DADOS COM IN (VALOR, VALOR, VALOR)
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

#APAGANDO DADOS COM BETWEEN (ENTRE 11 E 14)
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (11, 14))
#         conexao.commit()


#MUDANDO DADOS DA TABELA COM UPDATE
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('TOCA', 5))
        conexao.commit()


#MOSTRANDO DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes  ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)



