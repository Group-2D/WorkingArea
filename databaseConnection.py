### File is used to connect the database sever ### 


#libary imports 
import psycopg2

import databaseBuild


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

        self.dbCommit = self.dbConnection.commit()


        ##Methods 

        def closeConnection() -> None:
            self.dbCursor.close()
            self.dbConnection.close()
            return
        
        def buildDatabase(self) -> None:
            self.dbCursor.execute(
        
                """
                CREATE TABLE IF NOT EXSISTS modules(
                    mod_id SERIAL PRIMARY KEY,
                    mod_name VARCHAR(40) NOT NULL, 
                    mod_enrolled INT NOT NULL,
                    mod_lectures INT NOT NULL,
                    mod_practicals INT NOT NULL,
                    mod_tutorials INT NOT NULL
                );
                
                CREATE TABLE IF NOT EXSISTS lecturer(
                    lecturer_id SERIAL PRIMARY KEY,
                    lecturer_fname VARCHAR(20) NOT NULL,
                    lecturer_lname VARCHAR(20) NOT NUll,
                    lecturer_availability VARCHAR(100)
                );

                CREATE TABLE IF NOT EXSISTS building(
                    building_id SERIAL PRIMMARY KEY,
                    building_name VARCHAR(20)
                )

                CREATE TABLE IF NOT EXSISTS room(
                    room_id SERIAL PRIMARY KEY,
                    room_name VARCHAR(30),
                    room_capacity INT NOT NULL,
                    building_id INT NOT NULL REFERENCES building(building_id)
                );

                CREATE TABLE IF NOT EXSISTS lecture(
                    lecuture_id SERIAL PRIMARY KEY,
                    mod_id INT NOT NULL REFERENCES modules(mod_id),
                    room_id INT NOT NULL REFERENCES room(room_id),
                    lecturer_id INT NOT NULL REFERENCES lecturer(lecturer_id),
                    lecturer_start DECIMAL, 
                    lecturer_end DECIMAL
                );
                """
            )

            self.dbCommit()
            return 

def main() -> None:

    session = db()

    session.buildDatabase()

    session.dbCursor.execute(
        """SELECT * FROM modules"""
    )

    print(session.dbCursor.fetchall())

    session.closeConnection()


#driver 
if "__name__" == "__main__":
    main()