import psycopg2 
import dataValidation

#creates a modify data class with connection to the database
class ModifyData:
    def __init__(self):
        self.connectDb = psycopg2.connect(
            database = "timetable_gen",
            host = "",
            user = "",
            password = "",
            port = ""
            )
        
        #cursor variable uses the connection to the db to search and modify data 
        self.cursor = self.connectDb.cursor()

    #uses data as an array data[0] == module name
    #enter into a box -> "Core Computing", 300, 3, 1, 0
    def insertModuleData(self, data):

        if dataValidation.validateData('Module', data):
            self.cursor.execute(
                "INSERT INTO Modules (data) VALUES (%s, %s, %s, %s, %s)",
                (data[0],data[1], data[2], data[3], data[4])
            )
            
            self.commitChanges()
            return 
    
        else:
            return False

    #inserts data into the lecturer table
    def insertLecturerData(self, data):
        self.cursor.execute(
            "INSERT INTO Lecturer (data) VALUES (%s, %s, %s,)",
            (data[0], data[1], data[2])
        )

        self.commitChanges()
        return 


    #inserts data into the room table
    def insertRoomData(self, data):
        
        building_id = self.cursor.execute(
            "SELECT building_id FROM Building WHERE building_name = %s"
            (data[2])
        )

        self.cursor.execute(
            "INSERT INTO Room (data) VALUES (%s, %s, %s)",
            (data[0], data[1],building_id)
        )

        self.commitChanges()
        return 
    

    #inserts data into the building data 
    def insertBuildingData(self, building_name):
        self.cursor.execute(
            "INSERT INTO Building VALUES (%s)",
            (building_name)
        )

        self.commitChanges()
        return 

    #inserts data into the lecture table
    def insertLectureData(self, module_name, lecturer_name, room_name):
        module_id = self.cursor.execute(
            "SELECT module_id FROM module WHERE module_name = %s"
            (module_name)
        )
    
        lecturer_id = self.cursor.execute(
            "SELECT lecturer_id FROM Lecturer WHERE lecturer_name = %s"
            (lecturer_name)
        )

        room_id = self.cursor.execute(
            "SELECT room_id FROM Room WHERE room_name = %s"
            (room_name)
        )

        self.cursor.execute(
            "INSERT INTO Lecture VALUES (%s, %s, %s)"
            (module_id, lecturer_id, room_id)
        )

        self.commitChanges()
        return 
    
    #method used to commit changes to the database
    def commitChanges(self):
        self.cursor.commit()
        return 
    
    #removes selected data
    def deleteData(self, table_name, table_info, data):
        #check the table has data
        if self.getALLData() == None:
            return 0
        #remove data from table
        else:
            self.cursor.execute(
                "DELETE FROM %s WHERE %s = %s "
                (table_name,table_info, data)
            )

        self.commitChanges()
        return 
    
    #gets data
    def getALLData(self, table_name):
        self.cursor.execute(
            "SELECT * FROM %s"
            (table_name.upper())
        )

        return self.cursor.fetchall()
    
    def getData(self, table_name, data):
        
        self.cursor.execute(
            "SELECT * FROM %s WHERE VALUES (%s)"
            (table_name, data)
        )

        return self.cursor.fetchone()