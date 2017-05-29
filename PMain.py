import psycopg2

dbConnection = psycopg2.connect(host="localhost", user='postgres', password="postgres", dbname="Company")
dbCursor = dbConnection.cursor()

def Main():
    #Delete()
    Select()
    #Update()
    #Insert()


def Select():
    # dbCursor.execute("SELECT * FROM tbCompanies")
    # dbCursor.execute("SELECT * FROM tbCompanies WHERE id=%d"%3)
    # dbCursor.execute("SELECT * FROM tbCompanies WHERE nome=%s", ("teste%d"%2,))
    # dbCursor.execute("SELECT * FROM tbCompanies WHERE nome=%s", [1])
    try:
        dbCursor.execute("SELECT * FROM tbCompanies ORDER BY name")
        rows = dbCursor.fetchall()
        for row in rows:
            print(row[0], "-", row[1])
    except Exception as ex:
        print(ex)


def Insert():
    # itens = [(10, "teste10"), (11, "teste11"), (12, "teste12")]
    # dbCursor.executemany("INSERT INTO tbCompanies VALUES (%s, %s)", itens)
    # dbConnection.commit()
    try:
        for i in range(5):
           dbCursor.execute("INSERT INTO tbCompanies VALUES (%d, 'teste%d')"%(i, i))
        dbConnection.commit()
    except Exception as ex:
        print(ex)


def Update():
    try:
        dbCursor.execute("UPDATE tbCompanies SET name = %s WHERE index = %s", ("teste05", 0))
    except Exception as ex:
        print(ex)


def Delete():
    try:
        dbCursor.execute("DELETE FROM tbCompanies WHERE index = %s"% 0)
    except Exception as ex:
        print(ex)


def CreateTable():
    dbCursor.execute("CREATE TABLE tbCompanies (index INT, name TEXT)")
    dbConnection.commit()


Main()