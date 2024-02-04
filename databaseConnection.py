import pyscopg2 

#create connection to database for a session

connectDb = pyscopg2.connect(
    database = "",
    host = "",
    user = "",
    password = "",
    port = ""
    )

#Database - name of db to access
#Host - refers to db server ip address or url 
#User - Postgrese SQL user
#Password - Postgrese users password
#Port - locolhost port number on SQL server


#create cusor used to run quierries
cursor = connectDb.cursor()


#create functions to run quierries on the database
def getData():
    return

def insertData():
    return

def deleteData():
    return 