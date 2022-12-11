import re

class Laboratory:
    # addLabToFile
    def addLabToFile():
        file = open('Project Data\\files\laboratories.txt', 'a')
        Laboratory.enterLaboratoryInfo()            
        file.write('\n' + fileFormat)
        file.close()
        
    # writeListOfLabsToFile
    def writeListOfLabsToFile():
        file = open('Project Data\\files\laboratories.txt', 'w')
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
    def displayLabsList():
        file = open('laboratories.txt', 'r')
        Laboratory.readLaboratoriesFile()
        file.close()
    
    #readLaboratoriesFile
    def readLaboratoriesFile():
        file = open('laboratories.txt', 'r')
        for labSplit in file:
            lab, cost = labSplit.strip().split('_')
            headLab = re.findall('Lab', str(lab))
            headCost = re.findall('Cost', str(cost))
            for headLabName in headLab:
                for headCostName in headCost:
                    print('{:<15} {:<15}'.format(headLabName, headCostName))
            labArea = re.findall('\D+\d', str(lab))
            costArea = re.findall('\d\d+', str(cost))
            for labName in labArea:
                for labCost in costArea:
                    print('{:<15} {:<15}'.format(labName, labCost))
        file.close()

    def labMenu(self):
        while True:
            print('''Laboratories Menu:
            1 - Display laboratories list
            2 - Add Laboratory  /#Just make some changes here
            3 - Back to the Main Menu''')
            optionLab = int(input('Select Lab Menu: '))
            if optionLab == 1:
                Laboratory.displayLabsList()
            if optionLab == 2:
                Laboratory.addLabToFile()
            if optionLab == 3:
                break