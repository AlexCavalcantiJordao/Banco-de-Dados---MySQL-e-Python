import mysql.connector
form mysql.connector import Error
# Inserir registros em um banco de dados MySQL...
print("Rotina para cadastro de produtos no banco de dados.")
print("Entre com os dados conforme solicitado.")

idProd = input("ID do Produto: ")
nomeProd = input("Nome do Produto: ")
precoProd = input("Preço: ")
quantProd = input("Quantidade: ")

dados = idProd + ',\'' + nomeProd + '\',' + precoProd + ',' + quantProd + ')'
declaracao = """INSERT INTO tbl_produtos
(IdProduto, NomeProduto, Preco, Quantidade)
values("""
sql = declaracao + dados

try:
    con = mysql.connector.connect(host='localhost', database='db_MeusLivros', user='root', password='1234567')

    inserir_produtos = sql
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela !")
cursor.close()
except Error as erro:
    print("Falha ao inserir dados no MySQL: {}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizadas.")
