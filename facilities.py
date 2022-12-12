class Facility:
    facilities_list = []
    def __init__(self):
        pass

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def displayFacilities(self):
        self.facilities_list = []
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
        f = open("facilities.txt", "w")
        for item in self.facilities_list:
            f.writelines(item)
        f.close()
        
    def facilities_menu(self):
        while True:
            facilities_Input = int(input("""Facilities Menu:
            1 - Display Facilities list
            2 - Add Facility
            3 - Back to the Main Menu
            """))
            match facilities_Input:
                case 1:
                    self.displayFacilities()
                case 2:
                    self.addFacilities()
                    self.writeListOfFacilitiesToFile()
                case 3:
                    break

# facility = Facility("name")

#The above is commented out for now, may be reused for the final product to navigate through menus.
