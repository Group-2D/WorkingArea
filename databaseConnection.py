import psycopg2 

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
    
    #method used to get data 
    def getData(self, query):
        return 0
    
    #method used to insert data (likely to be split into seperate table methods)
    def insertData(self, data):
        return 0
    
    #uses data as an array data[0] == module name
    #enter into a box -> "Core Computing", 300, 3, 1, 0
    def insertModuleData(self, data):
        #check the length of the data list
        if data.isEmpty() or data.length() > 5:
            #check first index is a string
            return 0
        elif type(data[0]) != str:
            return 0

        else:        
            self.cursor.execute(
                "INSERT INTO Modules (data) VALUES (%s, %s, %s, %s, %s)",
                (data[0],data[1], data[2], data[3], data[4])
            )
    #removes selected data
    def deleteData(self, data):
        return 0