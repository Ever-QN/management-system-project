import doctors, facilities, lab, patients

while True:
    print('''Welcome to Alberta Hospital (AH) Management system
    Select from the following options, or select 0 to stop:
    1 - Doctors
    2 - Facilities
    3 - Laboratories
    4 - Patients''')
    mainMenu = int(input())
    if mainMenu == 1:
        # doctorsObject = doctors()
        # doctorsObject.docMenu()
        pass
    elif mainMenu == 2:
        # facilitiesObject = facilities()
        pass
    elif mainMenu == 3:
        # labObject = lab()
        pass
    elif mainMenu == 4:
        # patientsObject = patients()
        pass
    elif mainMenu == 0:
        break