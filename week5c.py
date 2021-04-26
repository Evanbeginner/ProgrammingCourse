def mainDisplay():
    print('What would you like to do')
    print('[a]Add new Students /t [b] View Students /t [q] Quit')
    choice = input('Type one letter (a/v/q)')
    return choice

def doAdd():
    students = []
    student = {}
    student["name"] = input('Enter name')
    students.append(student["name"])
    print(students)
    print('Add Function')

def doView():
    print('view function')

choice = mainDisplay()
while (choice != 'q') :
    if choice == 'a':
        doAdd()
    if choice == 'v':
        doView()
    else:
        choice = mainDisplay()