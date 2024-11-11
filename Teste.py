import pymysql.cursors

# Abrir uma conexão a u, banco de dados.....
 con = mysql.connector.connect(host='localhost', database='db_MeusLivros', user='root', password='1234567', cursorclass=pymysql.cursors.DictCursor)

# Preparar um cursor com o método .cursor()
with con.cursor() as c:
    # Criar uma consulta
    sql = "SELECT NomeLivro, ISBN13 FROM tbl_livros WHERE IdLivro = 104"
    c.execute(sql)
    res = c.fetchone()
    print(res)
    print()
    print("Livro Retornado: ", res['NomeLivro'])

    # Outras consultas: Dados da tabela de editoras....
    sql = "SELECT NomeEditora FROM tbl_editoras"
    c.execute(sql)
    res = c.fetchall()
    print("\n", res)
    print()
    for linha in res:
        print(linha['NomeEditora'])
        
con.close()
