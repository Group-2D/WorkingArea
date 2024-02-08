import psycopg2 

#creates a modify data class with connection to the database
class ModifyData:
    def __init__(self):
        self.connectDb = psycopg2.connect(
            database = "",
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
    
    #removes selected data
    def deleteData(self, data):
        return 0