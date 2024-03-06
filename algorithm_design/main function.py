
# dict containing times that a lecturer is busy
# format is dict = {"time":"lecturer"}
lecturerOccupied = {}

# the final timetable after all is said and done
# format is {"time":"lecture"}
finalTimetable = {}
# a dict/list of lectures that need to be inserted
# format is simply a list
lecturesToInsert = []

class currentLecture:

    # init method for class
    # requestedTime is timeslot that lecture is trying to occupy
    # students is a list of students in that lecture
    def __init__(
            self, 
            lectureName, 
            requestedTime, 
            lectureType, 
            students,
            proffessor):
        self.lectureName = lectureName
        self.requestedTime = requestedTime
        self.lectureType = lectureType
        self.students = students
        self.proffessor = proffessor
    

def pullLecturesFromDB():

    #
    # THIS FUNCTION REQUIRES
    # THE ALGORITHM TO DECIDE WHEN TO INSERT
    # THE ALGORITHM TO PULL LECTURES FROM THE DB
    # THE ALGORITHM TO ALLOCATE STUDENTS
    # USE THESE ALGORITHMS TO INSERT THE VALUES INTO THE VARIABLES BELOW
    #

    while True:
        name = ""
        time = ""
        lType = ""
        students = []

        lecturesToInsert.add(currentLecture(name,time,lType,students))


def retryTime(lecture):

    #
    # THIS FUNCTION GENERATES A NEW TIME TO BE INSERTED 
    # CALLS THIS FUNCTION WHEN THE LECTURE CANNOT BE INSERTED INTO THE CURRENT
    #   SELECTED TIME
    #

    lecture.time = ""
    return lecture


while len(lecturesToInsert) != 0:

    operatingLecture = lecturesToInsert[0]

    # first guard checks if the requestedTime is empty in the timetable
    # if it is empty, simply insert the lecture into that time then remove
    #   the lecture from the list of lectures to insert
    if finalTimetable[operatingLecture.requestedTime] == None:
        finalTimetable[operatingLecture.requestedTime] = (
            operatingLecture.lectureName)
        lecturesToInsert.remove(lecturesToInsert[0])
    
    elif finalTimetable[operatingLecture.requestedTime] != None:
        
        # this pulls the lecture taking up the timeslot into the variable
        #   "occupyingLecture"
        occupyingLecture = finalTimetable[operatingLecture.requestedTime.get()]

        # checks if the proffessor is busy at the requested time
        if operatingLecture.requestedTime in lecturerOccupied and (
            operatingLecture.proffessor) == (
            lecturerOccupied[operatingLecture.requestedTime]):
            
            # insertion failed, break to while, call functino for new time
            lecturesToInsert[0] = retryTime(operatingLecture)
        
        else:
            # checks if the lecture contains all students or some students
            if occupyingLecture.type == "Full":
                lecturesToInsert[0] = retryTime(operatingLecture)
            
            elif occupyingLecture.type == "Partial":

                # goes through student list for any non course wide lecture
                # if there are no student overlaps, insert
                for student in occupyingLecture.students:

                    if student in operatingLecture.students:
                        lecturesToInsert[0] = retryTime(operatingLecture)

                    else:
                        finalTimetable[operatingLecture.requestedTime] = (
                            operatingLecture.lectureName)
                        lecturesToInsert.remove(lecturesToInsert[0])