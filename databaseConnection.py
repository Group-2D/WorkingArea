

import psycopg2


dbConnection = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "Lebihan01!",
    port = 5432
)

dbCursor = dbConnection.cursor()

dbCursor.execute(
    """CREATE TABLE IF NOT EXISTS modules (
        mod_id SERIAL PRIMARY KEY,
        mod_name VARCHAR(40) NOT NULL, 
        mod_enrolled INT NOT NULL,
        mod_lectures INT NOT NULL,
        mod_practicals INT NOT NULL,
        mod_tutorials INT NOT NULL
    );
    """)

dbCursor.execute(
    """INSERT INTO module VALUES(
        
    )"""
)

print(dbCursor.fetchall())

dbCursor.commit()

dbCursor.close()
dbConnection.close()

