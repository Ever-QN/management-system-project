class Facility:
    facilities_list = []
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
            self.facilities_list.append(line)
        f.close()

    def addFacilities(self):
        newFacilityName = input("Enter facility name: ")
        self.facilities_list.append("\n" + newFacilityName)
        return newFacilityName


    def writeListOfFacilitiesToFile(self):
        f = open("facilitiestest.txt", "w")
        for item in self.facilities_list:
            f.writelines(item)
        f.close()