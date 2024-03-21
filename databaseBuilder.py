### File is used to build the Postgres SQL ###
from typing import Any

from typing import Any

def buildDatabaseSchema(dbCursor: Any, dbCommit: Any) -> None:
    dbCursor.execute(
        """
        CREATE TABLE IF NOT EXISTS modules(
            mod_id SERIAL PRIMARY KEY,
            mod_name VARCHAR(40) NOT NULL, 
            mod_enrolled INT NOT NULL,
            mod_lectures INT NOT NULL,
            mod_practicals INT NOT NULL,
            mod_tutorials INT NOT NULL,
            mod_hours_for_pract INT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS lecturer(
            lecturer_id SERIAL PRIMARY KEY,
            lecturer_title VARCHAR(5) NOT NULL,
            lecturer_fname VARCHAR(20) NOT NULL,
            lecturer_lname VARCHAR(20) NOT NULL,
            lecturer_modules VARCHAR(200) NOT NULL,
            lecturer_availability VARCHAR(50)
        );

        CREATE TABLE IF NOT EXISTS building(
            building_id SERIAL PRIMARY KEY,
            building_name VARCHAR(20)
        );

        CREATE TABLE IF NOT EXISTS room(
            room_id SERIAL PRIMARY KEY,
            room_name VARCHAR(30),
            room_capacity INT NOT NULL,
            building_id INT NOT NULL REFERENCES building(building_id),
            room_type VARCHAR(10) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS lecture(
            lecture_id SERIAL PRIMARY KEY,
            mod_id INT NOT NULL REFERENCES modules(mod_id),
            room_id INT NOT NULL REFERENCES room(room_id),
            lecturer_id INT NOT NULL REFERENCES lecturer(lecturer_id),
            lecture_type VARCHAR(10) NOT NULL,
            lecture_day DECIMAL NOT NULL,
            lecture_time DECIMAL NOT NULL
        );
        """
    )
    dbCommit()
    return

def insertDataToDb(dbCursor: Any, dbCommit: Any):
    dbCursor.execute(
        """INSERT INTO building (building_name) VALUES
        ('Angelesea'),
        ('Liongate'),
        ('Park'),
        ('Richmond');

        INSERT INTO lecturer (lecturer_title, lecturer_fname, lecturer_lname, lecturer_modules, lecturer_availability) VALUES
        ('Miss', 'Taylor', 'Swift', 'Architecture & Operating Systems', '000000000000000001000000001000000001000000001'),
        ('Mr','Adam', 'Levine', 'Networks', '000010010010000100001000001100000000000010000'),
        ('Mr', 'Lewis', 'Capaldi', 'Programming', '000000000000000000000000000000000000000000000'),
        ('Miss', 'Katy', 'Perry', 'Programming', '000000000000000000000000000000000000000000000');
        """)
    dbCommit()
    return
