import mysql.connector

try:
    # Criar conexão ao banco de dados....
    con = mysql.connector.connect(host='localhost',database='db_MeusLivros',user='root',password='1234567')

    # Declaração SQL a ser executada....
    criar_tabela_SQL = """CREATE TABLE tbl_produto(
                        IdProduto int(11) BOT NULL
                        NomeProduto VARCHAR(70) NOT NULL,
                        Preco FLOAT NOT NULL,
                        Quantidade TINYINT NULL,
                        PRIMARY KEY (IdProduto))"""

    # Criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de produto criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MySQL: {}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada.")
print("\nPróximo aula: Inserção de Registros na tabela criada.")
