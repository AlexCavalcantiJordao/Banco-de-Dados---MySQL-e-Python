import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='localhost',
        database='db_MeusLivros',
        user='root',
        password=''
    )

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()
        cursor.execute("SELECT DATABASE();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados", linha)

except Error as e:
    print("Erro ao conectar ao MySQL", e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada.")
