### File is used to build the Postgres SQL ###

from databaseConnection import db 

def buildDatabase() -> None:
    db.dbCursor.execute(
        
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

    db.dbCommit()

    return 
