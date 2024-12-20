import mysql.connector
from mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='db_MeusLivros', user='root', password='1234567')
    consulta_sql = "select * from tbl_autores"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    print("Número total de registro retornados: ", cursor.rowcount)

    print("\nMostrando os autores cadastrados.")
    for linha in linhas:
        print("Id: ", linha[0])
        print("Nome: ", linha[1])
        print("Sobrenome: ", linha[2], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrado.")
