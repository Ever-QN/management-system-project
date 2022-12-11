from doctors import Doctors
from facilities import Facility
from lab import Laboratory
from patients import Patients

doctorsInstance = Doctors()
facilityInstance = Facility()
labInstance = Laboratory()
patientsInstance = Patients()

while True:
    print('''Welcome to Alberta Hospital (AH) Management system
    Select from the following options, or select 0 to stop:
    1 - Doctors
    2 - Facilities
    3 - Laboratories
    4 - Patients''')
    mainMenu = int(input())
    if mainMenu == 1:
        doctorsInstance.docMenu()
    elif mainMenu == 2:
        facilityInstance.facilities_menu()
    elif mainMenu == 3:
        labInstance.labMenu()
    elif mainMenu == 4:
        patientsInstance.patients_menu()
    elif mainMenu == 0:
        break