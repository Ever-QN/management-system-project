class Patient:
    patients_list = []
    def __init__(self, pid, name, disease, gender, age):
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age

    def getPid(self):
        return self.__pid

    def setPid(self, newPid):
        self.__pid = newPid
    
    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getGender(self):
        return self.__disease

    def setDisease(self, newDisease):
        self.__disease = newDisease

    def getGender(self):
        return self.__gender

    def setGender(self, newGender):
        self.__gender = newGender

    def getAge(self):
        return self.__age

    def setAge(self, newAge):
        self.__age = newAge

    def formatPatientInfo(self):
        pass
    
    def enterPatientInfo(self):
        pass

    def readPatientsFile(self):
        f = open("patients.txt", "r")
        for lines in f.readlines():
            column = lines.split("_")
            patientObject = Patient(column[0], column,[1], column[2], column[3], column[4])
            self.patients_list.append(patientObject)
        f.close()

    def searchPatientById(self):
        pass

    def displayPatientInfo(self):
        pass

    def editPatientInfo(self):
        pass

    def displayPatientsList(self):
        for x in range(len(self.patients_list)):
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(self.patients_list[x].__pid, self.patients_list[x].__name, self.patients_list[x].__disease, self.patients_list[x].__gender, self.patients_list[x].__age))

    def writeListOfPatientsToFile(self):
        pass

    def addPatientToFile(self):
        pass