#  TEMP RULES:
#  All practs for a module will be in the same room.

# how do we associate one lecturer with the lecture and more than one with the practicals?
# how to make lecturers unavailable once they have been assigned to a lecture
# how to end the program if not spaces or availabilities can be found

import random
import time

#global variables

# maximum of 5 days, 9 hour slots, 12 rooms
timetableEntries = [[[None for _ in range(8)] for _ in range(9)] for _ in range(5)] #days, hour slots, rooms
numOfModules = 6

# modules variables
modules_list = []
modName = ["Architecture & Operating Systems", "Comp Tutorial 4", "Core Computing Concepts", "Database System Development", "Networks", "Programming"]
lecHours = [1, 0, 1, 1, 1, 1] 
practHours = [2, 0, 1, 2, 1, 2] 
tutHours = [0, 1, 0, 0, 0, 0]
numOfStudents = [200, 200, 200, 200, 200, 150]

# rooms variables
#room name, building name, capacity, type
roomsList = [
                ["A2.03", "Anglesea", 40, "pract"],
                ["FTC_Floor1", "FutureTechnologyCentre", 80, "pract"], ["FTC_Floor2", "FutureTechnologyCentre", 80, "pract"], ["FTC_Floor1", "FutureTechnologyCentre", 50, "tut"],
                ["L0.14a", "LionGate", 67, "tut"],
                ["RLT1", "Richmond Building", 330, "lec"], ["RLT2", "Richmond Building", 160, "lec"], ["R1.03", "Richmond Building", 24, "pract"],
            ]

# lecturer variables
lecturersList = [
                    ['John','Smith', 'Architecture & Operating Systems, Programming, Comp Tutorial 4', 'EX001'],
                    ['Lisa','Franklin', 'Core Computing Concepts', 'EX003'],
                    ['Herbert','Jones', 'Core Computing Concepts', 'EX009'],
                    ['Richard','Johnson', 'Database Systems Development', 'EX004'],
                    ['Hugh','Piper','Programming', 'EX006'],
                    ['Javier','Rodriguez', 'Networks', 'EX007'],
                    ['Kathlyn','Ferguson', 'Networks', 'EX008']
                ]

#tidy variables/arrays
modsCompleted = []

class ModuleInfo:
    def __init__(self, mod_name, lec_hours, pract_hours, tut_hours, num_of_students):
        self.modName = mod_name
        self.lecHours = lec_hours
        self.practHours = pract_hours
        self.tutHours = tut_hours
        self.numOfStudents = num_of_students
        
class Room:
    def __init__(self, room_name, building, room_type, capacity):
        self.roomName = room_name
        self.buildingName = building
        self.roomType = room_type
        self.roomcapacity = capacity

class Lecturer:
    def __init__(self, lecturer_name, modules):
        self.lecturerName = lecturer_name
        self.modulesTaught = modules



def createModuleClasses():
    for i in range(0, len(modName)):
        mod_name = modName[i]
        lec_hours = lecHours[i]
        pract_hours = practHours[i]
        tut_hours = tutHours[i]
        num_of_students = numOfStudents[i]

        new_module = ModuleInfo(mod_name, lec_hours, pract_hours, tut_hours, num_of_students)
        modules_list.append(new_module)


def determineAvailableLecturers(module_info, availableLecturers):
    for i in range(0, len(lecturersList)):
        #print(lecturersList[2][2])
        #print(module_info.modName)
        if module_info.modName in lecturersList [i][2]:
            print("Hey")
            availableLecturers.append(lecturersList[i])

        return availableLecturers


def checkConstraints(module_info, type, randPotentialRoom, studentsUnassigned, room):
    # 5 days, 9 hour slots
    randDay = random.randint(0, 4) 
    randHour = random.randint(0, 8)
    print(randDay, randHour)
    #time.sleep(2)
    
    if timetableEntries [randDay] [randHour] [randPotentialRoom] is None:
        availableLecturers = determineAvailableLecturers(module_info, availableLecturers)

        #print(availableLecturers)
        print("Hello")

        randLecturer = [random.randint(0, len(availableLecturers))]
        
        #figure out how lecturers can have available and unavailable times
        for i in range(len(availableLecturers)):
            #for i in numLecturersRequired:
                
                timetableEntries[randDay][randHour][randPotentialRoom] = [module_info.modName, type, randLecturer, room]
                print(f"Room info: {room}")

                if type == 'lec':
                    studentsUnassigned = studentsUnassigned - room [2] 
                    print(f"Students unassigned: {studentsUnassigned} ")

                time.sleep(100)



def insertIntoTimetable(module_info, type):
    room = ""
    studentsUnassigned = module_info.numOfStudents
    moduleInserted = False
    availableLecturers = []

    print(f"{module_info.modName} {type}") 
    
    match type:
        case 'lec':
            hoursUnassigned = module_info.lecHours
        case 'pract':
            hoursUnassigned = module_info.practHours
        case 'tut':
            hoursUnassigned = module_info.tutHours

    while moduleInserted == False:
        correctRoomType = False

        while correctRoomType == False:
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            #checks that the room is the correct type for the sessions being assigned to
            #print(roomsList[0])

            if roomsList[randPotentialRoom] [3] == type:
                room = roomsList[randPotentialRoom]
                correctRoomType = True 
        
        if type == "lec":
            checkConstraints(module_info, type, randPotentialRoom, studentsUnassigned, room)
        
        else:
            #makes new entries in the timetable until every student has been assigned to a session
            while studentsUnassigned > 0:
                checkConstraints(module_info, type, randPotentialRoom, studentsUnassigned, room)
                    
            
def displayTimetable():
    for i in range(len(timetableEntries)):
        for j in range(len(timetableEntries[i])):
            for k in range(len(timetableEntries[i][j])):
                print(f"Value at ({i}, {j}, {k}): {timetableEntries [i] [j] [k]}")





def main():
    #declare variables
    modulesCompleted = []

    #create class for the module which takes in mod information.
    createModuleClasses() 


    for i in range(numOfModules):
        moduleInserted = False 

        while moduleInserted == False:
            randMod = random.randint(0, numOfModules-1) 

            if randMod not in modulesCompleted:
                if modules_list[randMod].lecHours > 0:
                    for i in range(lecHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'lec')

                if modules_list[randMod].practHours > 0:
                    for i in range(practHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'pract')

                if modules_list[randMod].tutHours > 0:
                    for i in range(tutHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'tut')

                moduleInserted == True
            
        modulesCompleted.append(randMod) 

    #test print
    displayTimetable()

main()