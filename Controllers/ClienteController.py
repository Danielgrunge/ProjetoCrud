import services.database as db;



def incluir(cliente):

    db.curs.execute("""INSERT INTO cliente(clinome, cliidade, cliprofissao) VALUES (%s,%s,%s)""",
    (cliente.nome, cliente.idade, cliente.profissao))

    db.connection.commit()
    count = db.curs.rowcount
    print(count, "Record inserted successfully into mobile table")



    # sql_insert = """INSERT INTO cliente(clinome, cliindade, cliprofissao) VALUES (%s,%s,%s)"""
    # dados = cliente.nome, cliente.idade, cliente.profissao
    # db.curs.execute(sql_insert, dados)
    # db.connection.commit()
    # count = db.cursor.rowcount
    # print(count, "Record inserted successfully into mobile table")
