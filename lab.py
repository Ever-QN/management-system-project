import re

class Laboratory:
    labList = []
    def __init__(self, lab = "", cost = ""):
        self.__lab = lab
        self.__cost = cost
        
    def getLab(self):
        return self.__lab
    
    def setLab(self, lab):
        self.__lab = lab
        
    def getCost(self):
        return self.__cost
    
    def setCost(self, cost):
        self.__cost = cost
                
    def __str__(self):
        return f"My {self.__lab} is ${self.__cost}"
    
    def formatLab(self):
        print(self.__lab, '_', self.__cost)

    # addLabToFile
    def addLabToFile():
        file = open('laboratories.txt', 'a')
        Laboratory.enterLaboratoryInfo()            
        file.write('\n' + fileFormat)
        file.close()
        
    # writeListOfLabsToFile
    def writeListOfLabsToFile():
        file = open('laboratories.txt', 'w')
        global inputLab
        global inputCost
        numberLab = int(input('How many lab you want to write: '))
        file.write('Lab_Cost')
        number = numberLab
        ite = 0
        for ite in range(number):
            ite += 1
            if ite <= number:
                Laboratory.enterLaboratoryInfo()
                file.write('\n' + fileFormat)
            else:
                break
        file.close()

    # enterLaboratoryInfo
    def enterLaboratoryInfo():
        file = open('laboratories.txt', 'a')
        global inputLab
        global inputCost
        inputLab = str(input('Please enter Lab Name: '))
        inputCost = int(input('Please enter Lab Cost: '))
        Laboratory.formatDrInfo()
   
    # formatDrInfo
    def formatDrInfo():
        global fileFormat
        fileFormat = ("{0}_{1}".format(inputLab, inputCost))
    
    # displayLabList
    def displayLabsList(self):
        for line in range(len(self.labList)):
            print("{:<15} {:<15}".format(self.labList[line].__lab, self.labList[line].__cost))
    
    #readLaboratoriesFile
    def readLaboratoriesFile(self):
        file = open('laboratories.txt', 'r')
        readLines = file.readlines()
        for labSplit in readLines:
            labLine = labSplit.split('_')
            labItem = Laboratory(labLine[0], labLine[1])
            self.labList.append(labItem)
        
    def clearLabList(self):
        self.labList.clear()

    def labMenu():
        while True:
            print('''Laboratories Menu:
            1 - Display laboratories list
            2 - Add Laboratory
            3 - Back to the Main Menu''')
            optionLab = int(input('Select Lab Menu: '))
            if optionLab == 1:
                Laboratory().readLaboratoriesFile()
                Laboratory().displayLabsList()
                Laboratory().clearLabList()
            if optionLab == 2:
                Laboratory.addLabToFile()
            if optionLab == 3:
                break
