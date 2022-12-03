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
        file = open('Project Data\\files\laboratories.txt', 'a')
        global inputLab
        global inputCost
        numberLab = int(input('How many lab you want to write: '))
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
        file = open('Project Data\\files\laboratories.txt', 'a')
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
        file = open('Project Data\\files\laboratories.txt', 'r')
        print('{:<15} {:<15}'.format('Lab','Cost'))
        Laboratory.readLaboratoriesFile()
        file.close()
    
    #readLaboratoriesFile
    def readLaboratoriesFile():
        file = open('Project Data\\files\laboratories.txt', 'r')
        global labInfo
        global labArea
        global labCost
        for labSplit in file:
            lab, cost = labSplit.strip().split('_')
            labArea = re.findall('\D+\d', str(lab))
            costArea = re.findall('\d\d+', str(cost))
            for labName in labArea:
                for labCost in costArea:
                    labName, labCost
                    print('{:<15} {:<15}'.format(labName, labCost))
        file.close()

print('''Laboratories Menu:
      1 - Display laboratories list
      2 - Add Laboratory  /#Just make some changes here
      3 - Back to the Main Menu''')
displayLab = 1
addLab = 2
backMenu = 3
while True:
    optionLab = int(input('Select Lab Menu: '))
    if optionLab == 1:
        Laboratory.displayLabsList()
    if optionLab == 2:
        Laboratory.addLabToFile()
    if optionLab == 3:
        break
    