class Patient:
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