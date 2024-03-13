'''
> implement a method to iterate through rawModuleList and apply 
    splitModuleIntoClass function on each element

> database needs to include what subjects a professor can teach
> database needs to include how many classes each module has, and the type and
    capacity of each class

> how is professor availability being stored/handled

> need to have a prepared list of what is being sorted/pulled from the database

'''

# list containing all the professors in the course of objects Professor
# used in determining whether professors are avialable, etc.
professorList = []


# a dict/list of lectures that need to be inserted
# format is a list of objects from class 'Lecture'
lecturesToInsert = []

# how many students in the whole school
studentsInSchool = 250

class Lecture:

    # requestedTime is timeslot that lecture is trying to occupy
    # students is a list of students in that lecture
    def __init__(
            self, 
            moduleName,
            classNumber,
            lectureType):
        self.moduleName = moduleName
        self.classNumber = classNumber
        self.lectureType = lectureType
        self.requestedTime = None
        self.students = None
        self.professor = None


class Professor:
    
    # teachableSubjects is the subjects that the professor can teach
    def __init__(
            self,
            professorFName,
            professorLName,
            teachableSubjects,
            availability
    ):
        self.name = professorFName + " " + professorLName
        self.teachableSubjects = teachableSubjects
        self.availability = availability


def pullRawFromDB():

    rawStudents = []
    rawModules = []
    rawProfessors = []
    rawRooms = []

    # to pull from DB still;
    #   how many classes per module?
    #   are they full classes or partial classes?
    #
    #   what can each professor teach?
    #   what is each professors availability
    #
    #   what modules is each student taking?
    #
    #   what is the capacity of each room?


def splitModuleIntoClass(moduleName, classes):

    # 'moduleName' is simply the name of the module
    # 'classes' is a list of tuples
    # each tuple is a type (FULL, PARTIAL) and capacity
    for (classType, capacity) in classes:

        if classType == "FULL":

            lecturesToInsert.add(Lecture(
                moduleName= moduleName, 
                classNumber= 1, 
                lectureType= "FULL"))
        
        else:
            iterations = 1

            while capacity < studentsInSchool:

                # inserts a lecture with incrementing classnumber for as many
                #   classes as necessary to ensure each student has a class
                lecturesToInsert.add(Lecture(
                    moduleName= moduleName, 
                    classNumber= iterations, 
                    lectureType= "PARTIAL"))

                iterations += 1
                capacity += capacity


def listProfessors():

    # profesor data taken from 'rawProfessors'
    # professor list is formatted as list of objects in 'professorList'
    #   of class 'Professor'
    # this function only exists since i dont know the format of data being
    #   pulled from the database, and it'll likely need cleaning
    
    professorList = []

    # this function will also fill out a professors teachableSubjects and
    #   availability


def assignProfToClass():
    pass


def createStudentList():
    pass


def assignStudentsToClasses():
    pass


def prepareClassesList():
    pass

