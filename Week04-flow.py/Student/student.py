StudentInfo = {'Student' : 'Mary', 'modules': [{'coursename': 'Programming', 'grade':45 }, {'coursename': 'History', 'grade' : 67 } ] }

print('Student : {} '. format(StudentInfo['Student']))

for module in StudentInfo['modules']:
   print('Course :  {}  ... Grade : {} '. format(module['coursename'],module['grade']))


def maindisplay():
    print('What would you like to do ')
    print('[a] Add new Student')
    print('[v] View Student')
    print('[q] Quit')
    choice = input('Type one letter (a/v/q):')
    return choice
    
def doAdd() :
    Students = []
    Students['name'] = str(input('Please Enter Student Name'))
    Students.append
    


def doView() :
    print('add code here')



choice = maindisplay()
while choice != 'q':
    if choice == 'a' :
        doAdd()
    elif choice == 'v' :
        doView()
    elif choice !='q':
        print('Please select a/v/q')

print('Program has ended')
