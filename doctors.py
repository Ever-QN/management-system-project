class Doctors:
    doc_list =[]
    global option
   
    def __init__(self, id='', name='', specialize='', worktime='', qualification='', rmnum=''):
            self.__id = id
            self.__name = name
            self.__specialize = specialize
            self.__worktime = worktime
            self.__qualification = qualification
            self.__rmnum = rmnum
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getName(self):
        return self.__name
    
    def setName(self, name):  
        self.__name = name

    def getName(self):
        return self.__specialize
    
    def setName(self, specialize):  
        self.__specialize = specialize

    def getName(self):
        return self.__worktime
    
    def setName(self, worktime):  
        self.__worktime = worktime

    def setName(self, specialize):  
        self.__specialize = specialize

    def getName(self):
        return self.__qualification
    
    def setName(self, qualification):  
        self.__qualification = qualification
    
    def getId(self):
        return self.__rmnum
    
    def setId(self, rmnum):
        self.__rmnum = rmnum

    def __str__(self):
        return f"{self.__id} {self.__name} {self.__specialize} {self.__worktime} {self.__qualification} {self.__rmnum}"

    def formatDrInfo(self, list):
        return '_'.join(list) + "\n"

    def enterDrInfo(self):
        new_doc = []

        new_id = input('Enter the doctor ID: ')
        new_doc.append(new_id)
        new_name = input('Enter new name: ')
        new_doc.append(new_name)
        new_specialize = input('Enter new Specilist in: ')
        new_doc.append(new_specialize)
        new_worktime = input('Enter new timing: ')
        new_doc.append(new_worktime)
        new_qualification = input('Enter new qualication: ')
        new_doc.append(new_qualification)
        new_rmnum = input('Enter new room number: ')
        new_doc.append(new_rmnum)

        return new_doc
        
    def readDoctorsFile(self):
        self.doc_list = []
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for l in lines:
            docs = l.split("_")
            doctorObject = Doctors(docs[0], docs[1], docs[2], docs[3], docs[4], docs[5])
            self.doc_list.append(doctorObject)
        return self.doc_list

    def searchDoctorById(self):
        input_id = input('Enter the doctor Id: ')
        self.displayDoctorInfo(input_id)

    def searchDoctorByName(self):
        input_name = input('Enter the doctor name: ')
        self.displayDoctorInfo(input_name)

    def displayDoctorInfo(self, uinput):
        for d in range(len(self.doc_list)):
            if uinput == self.doc_list[d].__id or uinput == self.doc_list[d].__name:
                print("{:<5} {:<23} {:<15} {:<15} {:<15} {:<15}".format(self.doc_list[0].__id, self.doc_list[0].__name, self.doc_list[0].__specialize, self.doc_list[0].__worktime, self.doc_list[0].__qualification, self.doc_list[0].__rmnum))
                print("{:<5} {:<23} {:<15} {:<15} {:<15} {:<15}".format(self.doc_list[d].__id, self.doc_list[d].__name, self.doc_list[d].__specialize, self.doc_list[d].__worktime, self.doc_list[d].__qualification, self.doc_list[d].__rmnum))
                break
        else:
            print("Can't find the doctor with the same id/name in the system")

    def editDoctorInfo(self):
        new_doc = []
        uinput2 = input('Please enter the id of the doctor that you want to edit their information: ')
        with open("doctors.txt", "r") as freader:
            l = freader.readlines()
            for d in range(len(self.doc_list)):
                if uinput2 == self.doc_list[d].__id:
                    new_doc.append(uinput2)
                    new_name = input('Enter new name: ')
                    new_doc.append(new_name)
                    new_specialize = input('Enter new Specilist in: ')
                    new_doc.append(new_specialize)
                    new_worktime = input('Enter new timing: ')
                    new_doc.append(new_worktime)
                    new_qualification = input('Enter new qualication: ')
                    new_doc.append(new_qualification)
                    new_rmnum = input('Enter new room number: ')
                    new_doc.append(new_rmnum)
        
                    l[d] = self.formatDrInfo(new_doc)
                    with open("doctors.txt") as fwriter:
                        for line in l:
                            fwriter.write(line)
                    break                        
        freader.close()
        fwriter.close()

    def displayDoctocsList(self):
        for d in range(len(self.doc_list)):
            print('{:<5} {:<23} {:<15} {:<15} {:<15} {:<15}'.format(self.doc_list[d].__id, self.doc_list[d].__name, self.doc_list[d].__specialize, self.doc_list[d].__worktime, self.doc_list[d].__qualification, self.doc_list[d].__rmnum))

    def writeListOfDoctorsToFile(self, doctors_list):
        with open("doctors.txt", "w") as f:
            f.write(doctors_list)

    def addDrToFile(self):
        doclist = self.formatDrInfo(self.enterDrInfo())
        with open("doctors.txt", "a") as f:
            f.write(doclist)
        f.close()

    def docMenu(self):
        while True:
            print('\nDoctors Menu:')
            print('1 - Display Doctors list')
            print('2 - Search for doctor by id')
            print('3 - Search doctor by name')
            print('4 - Add doctor')
            print('5 - Edit doctor info')
            print('6 - Back to the Main Menu')
            option = str(input())

            if option == '0':
                break

            self.readDoctorsFile()

            if option == '1':
                self.displayDoctocsList()
                self.readDoctorsFile()
            elif option == '2':
                self.searchDoctorById()
            elif option == '3':
                self.searchDoctorByName()
            elif option == '4':
                self.addDrToFile()
            elif option == '5':
                self.editDoctorInfo()
            elif option == '6':
                break
