students = []
def readmodules():
    modules = {}
    modules['subject'] = input('Enter subject')
    modules['grade'] = input('Enter grade')
    students.append(modules)

def doadd(students):
    currentstudents = {}
    currentstudents['name'] = input('enter name')
    currentstudents['modules'] = readmodules()
    students.append(currentstudents)
    readmodules()


doadd(students)

print(students)