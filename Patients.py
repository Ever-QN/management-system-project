class Patients:
    patients_list = []
    def __init__(self, pid="", name="", disease="", gender="", age=""):
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

    def __str__(self):
        return f"{self.__pid} {self.__name} {self.__disease} {self.__gender} {self.__age}"
    
    def __repr__(self):
        return str(self)

    def formatPatientInfo(self, patient_list_info):
        return "_".join(patient_list_info) + "\n"
    
    def enterPatientInfo(self):
        patient_Info = []
        newPatientID = input("Enter patient id (pid): ")
        newPatientName = input("Enter patient name: ")
        newPatientDisease = input("Enter patient disease: ")
        newPatientGender = input("Enter patient gender (male or female): ")
        newPatientAge = input("Enter patient age: ")
        patient_Info.append(newPatientID)
        patient_Info.append(newPatientName)
        patient_Info.append(newPatientDisease)
        patient_Info.append(newPatientGender)
        patient_Info.append(newPatientAge)
        return patient_Info

    def readPatientsFile(self):
        f = open("patients.txt", "r")
        for line in f.readlines():
            column = line.split("_")
            patientObject = Patients(column[0], column[1], column[2], column [3], column[4])
            self.patients_list.append(patientObject)

    def searchPatientById(self):
        userInput = input("Enter the patient Id: ")
        self.displayPatientInfo(userInput)

    def displayPatientInfo(self, input):
        success = False
        for x in range(len(self.patients_list)):
            if input != self.patients_list[x].__pid:
                success = False
            elif input == self.patients_list[x].__pid:
                success = True
                break

        if success:
            print(f"{self.patients_list[x].__pid:<5} {self.patients_list[x].__name:<15} {self.patients_list[x].__disease:<10} {self.patients_list[x].__gender:<10} {self.patients_list[x].__age:<5}")
        elif success == False:
            print("Can't find the patient with the same id in the system")
        pass

    def editPatientInfo(self):
        userInput = input("Please enter the id of the Patient that you want to edit their information: ")
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            edit_Patient_Info = []
            for x in range(len(self.patients_list)):
                if userInput == self.patients_list[x].__pid:
                    patientID = userInput
                    print(self.patients_list)
                    newPatientName = input("Enter patient name: ")
                    newPatientDisease = input("Enter patient disease: ")
                    newPatientGender = input("Enter patient gender (male or female): ")
                    newPatientAge = input("Enter patient age: ")
                    edit_Patient_Info.append(patientID)
                    edit_Patient_Info.append(newPatientName)
                    edit_Patient_Info.append(newPatientDisease)
                    edit_Patient_Info.append(newPatientGender)
                    edit_Patient_Info.append(newPatientAge)
                    lines[x] = self.formatPatientInfo(edit_Patient_Info)
                    with open("patients.txt", "w") as file:
                        for line in lines:
                            file.write(line)
                    

    def displayPatientsList(self):
        for x in range(len(self.patients_list)):
            print(f"{self.patients_list[x].__pid:<5} {self.patients_list[x].__name:<15} {self.patients_list[x].__disease:<10} {self.patients_list[x].__gender:<10} {self.patients_list[x].__age:<5}")

    def writeListOfPatientsToFile(self):
        pass

    def addPatientToFile(self):
        pass 





displayInfo = Patients()
displayInfo.readPatientsFile()
displayInfo.displayPatientsList()
# displayInfo.searchPatientById()

displayInfo.editPatientInfo()