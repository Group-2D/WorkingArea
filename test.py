from databaseManger import session


session.dbCursor.execute(
    """SELECT * FROM building;"""
)

for row in session.dbCursor.fetchall():
    print(row)

session.dbCommit

session.dbClose()