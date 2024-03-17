### File is used to connect the database sever ### 


#libary imports 
import psycopg2


class db:

    def __init__ (self) -> None:

        #Attributes

        self.dbConnection = psycopg2.connect(
            host = "localhost",
            database = "timetable_gen",
            user = "postgres",
            password = "Lebihan01!",
            port = 5432
         )
        
        self.dbCursor = self.dbConnection.cursor()

        self.dbExecute = self.dbCursor.execute()


        ##Methods 

        def closeConnection(self) -> None:
            self.dbCusor.close()
            self.dbConnection.close()
            return


        

