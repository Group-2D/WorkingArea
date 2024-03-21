import psycopg2
from psycopg2 import sql
from typing import Any

from .databaseBuilder import buildDatabaseSchema, insertDataToDb


class dbManger:
    
    def __init__(self) -> None:
        self.dbConnection = psycopg2.connect(
            host = "localhost",
            dbname = "TimetableDB",
            user = "postgres",
            password = "Jimbobrimbo9",
            port = 5432
        )

        self.dbCursor = self.dbConnection.cursor()

        self.dbCommit = self.dbConnection.commit()

    def dbClose(self):
        self.dbCursor.close()
        self.dbConnection.close()
    
    def selectAll(self, table: str):
        self.dbCursor.execute(
            """SELECT * FROM %s """ % table
        )

        for row in self.dbCursor.fetchall():
            print(row)
        
        return
    

    def selectNumOfEntries(self, tbl_name: str):
        # ! Error occurs: 'Composed' object is not subscriptable
        self.dbCursor.execute( 
            query = sql.SQL("select count(*) from {table}").format(
                table = sql.Identifier(tbl_name),
                )
        )
        return self.dbCursor.fetchall()

    
    def selectOnCondition(self, tbl_field: str, tbl_name: str, target: str, value: Any):
        # ! Error occurs: 'Composed' object is not subscriptable
        self.dbCursor.execute( 
            query = sql.SQL("select {field} from {table} where {condition} = %s").format(
                field = sql.Identifier(tbl_field),
                table = sql.Identifier(tbl_name),
                condition = sql.Identifier(target))
                [value]
        )
        return self.dbCursor.fetchall()

    def insertIntoDb(self, tbl_name: str, tbl_cols: str, value: Any) -> None:
        
        self.dbCursor.execute(
            sql.SQL("insert into {table} ({column}) values (%s)").format(
                table = sql.Identifier(tbl_name),
                column = sql.Identifier(tbl_cols)),
                [value]
            )
        return 
    
    def removeDataEqual(self, tbl_name: str, tbl_column: str, value: Any) -> None:
        self.dbCursor.execute(
            sql.SQL("DELETE FROM {table} WHERE {column} = %s").format(
                table = sql.Identifier(tbl_name),
                column = sql.Identifier(tbl_column)),
                [value]
            )

        return

    def removeTable(self, tbl_name: str) -> None:
        self.dbCursor.execute(
            """DROP TABLE IF EXISTS %s CASCADE;""" % tbl_name
        )

        return 

session = dbManger()

buildDatabaseSchema(session.dbCursor)
insertDataToDb(session.dbCursor)

session.dbCommit

session.selectAll('lecturer')

session.dbClose