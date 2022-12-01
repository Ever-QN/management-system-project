class Facility:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def displayFacilities(self):
        f = open("facilities.txt", "r")
        for line in f.readlines():
            print(line)
        f.close()

    def addFacilities(self):
        pass

    def writeListOfFacilitiesToFile(self):
        pass

