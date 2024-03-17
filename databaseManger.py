import psycopg2
from psycopg2 import sql

from databaseBuilder import buildDatabaseSchema, insertDataToDb


class dbManger:

    def __init__(self) -> None:
        self.dbConnection = psycopg2.connect(
            host = "localhost",
            dbname = "postgres",
            user = "postgres",
            password = "Lebihan01!",
            port = 5432
        )

        self.dbCursor = self.dbConnection.cursor()

        self.dbCommit = self.dbConnection.commit()

    def dbClose(self):
        self.dbCursor.close()
        self.dbConnection.close()
    
    def selectAll(self, table):
        self.dbCursor.execute(
            """SELECT * FROM %s """ % table
        )

        for row in self.dbCursor.fetchall():
            print(row)
        
        return

    def insertIntoDb(self, tbl_name, tbl_cols, value):
        self.dbCursor.execute(
            sql.SQL("insert into {table} ({column}) values (%s)").format(
                table = sql.Identifier(tbl_name),
                column = sql.Identifier(tbl_cols)),
                [value]
            )
        return 


session = dbManger()

buildDatabaseSchema(session.dbCursor, session.dbCommit)
insertDataToDb(session.dbCursor, session.dbCommit)

session.selectAll('building')

session.insertIntoDb('building', 'building_name','Libiary')
print()
session.selectAll('building')

session.dbCommit


