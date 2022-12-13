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
        return "_".join(patient_list_info)
    
    def enterPatientInfo(self):
        patient_info = []
        newPatientID = input("Enter patient id (pid): ")
        newPatientName = input("Enter patient name: ")
        newPatientDisease = input("Enter patient disease: ")
        newPatientGender = input("Enter patient gender (male or female): ")
        newPatientAge = input("Enter patient age: ")
        patient_info.append(newPatientID)
        patient_info.append(newPatientName)
        patient_info.append(newPatientDisease)
        patient_info.append(newPatientGender)
        patient_info.append(newPatientAge)
        self.addPatientToFile(patient_info)
        return patient_info

    def readPatientsFile(self):
        self.patients_list = []
        f = open("patients.txt", "r")
        for line in f.readlines():
            column = line.split("_")
            patientObject = Patients(column[0], column[1], column[2], column [3], column[4])
            self.patients_list.append(patientObject)
        return self.patients_list

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

    def editPatientInfo(self):
        userInput = input("Please enter the id of the Patient that you want to edit their information: ")
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            edit_patient_info = []
            for x in range(len(self.patients_list)):
                if userInput == self.patients_list[x].__pid:
                    patientID = userInput
                    newPatientName = input("Enter patient name: ")
                    newPatientDisease = input("Enter patient disease: ")
                    newPatientGender = input("Enter patient gender (male or female): ")
                    newPatientAge = input("Enter patient age: ")
                    edit_patient_info.append(patientID)
                    edit_patient_info.append(newPatientName)
                    edit_patient_info.append(newPatientDisease)
                    edit_patient_info.append(newPatientGender)
                    edit_patient_info.append(newPatientAge)
                    edit_patient_info = edit_patient_info[-1] + "\n"
                    lines[x] = self.formatPatientInfo(edit_patient_info)
                    with open("patients.txt", "w") as file:
                        for line in lines:
                            file.write(line)


    def displayPatientsList(self):
        self.readPatientsFile()
        for x in range(len(self.patients_list)):
            print(f"{self.patients_list[x].__pid:<5} {self.patients_list[x].__name:<15} {self.patients_list[x].__disease:<10} {self.patients_list[x].__gender:<10} {self.patients_list[x].__age:<5}")

    def writeListOfPatientsToFile(self, patients_list):
        with open("patients.txt", "w") as file:
                file.write(patients_list)

    def addPatientToFile(self, new_patient_info):
        with open("patients.txt", "a") as file:
            new_patient_info = self.formatPatientInfo(new_patient_info)
            file.write("\n" + new_patient_info)

    def patients_menu(self):
        while True:
            patients_Input = int(input("""Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu
"""))
            match patients_Input:
                case 1:
                    self.displayPatientsList()
                case 2:
                    self.searchPatientById()
                case 3:
                    self.enterPatientInfo()
                case 4:
                    self.editPatientInfo()
                case 5:
                    break
