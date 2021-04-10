SP = int(input('Please Enter Student Grade : '))

if SP < 0 or SP > 100:
 print('Please Enter a number between 0 and 100')
elif SP < 40 :
 print('Fail')
elif SP < 50 :
 print('Pass')
elif SP < 60:
 print('Merit 2')
elif SP < 70 :
 print('Merit 1')
else:
 print('Distinction')
  




         