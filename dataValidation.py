#file is used to validate data that is inputed by the user 


def validateData(selectedTbl, data):
    
    if selectedTbl == 'Module':
        if (validateModuleData(data)):
            return True 
        else:
            return False



def validateModuleData(data):
    #check list length is equal to 5

    if data.length != 5:

        if data.length < 5:

            for i in range(5 - data.length):
                data.append(0)
        

        else:
            return False, data
        
    #type check each position (data[0] = str, data[1]... = int)

    if type(data[0]) != 'str':
        return False
    
    else:
        for i in range(len(data)-1):
            if type(data[i+1]) != 'Int':
                try:
                    data[i+1] = int(data[i+1])
                except:
                    ValueError
                    return False, data

    return True, data

def validateLecturerData(data):
    return 0 

def validateRoomData(data):
    return 0 

def validateBuildingData(data):
    return 0 

def validateLecturerData(data):
    return 0

def validateDeleteData(data):
    return 0 





#the cases the data needs to validated
    #1. the length of the array is different for each table
    #2. The position of each piece of data is different
    #3. Type Checkes on the data, perform any conversions if nessacary

