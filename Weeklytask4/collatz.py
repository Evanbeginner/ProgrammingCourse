Number = int(input('Enter number'))
while Number != 1:
 if Number > 0:
   if Number % 2 == 0:
      print(Number)
      Number = Number/2
   else: 
       print(Number)
       Number = (Number*3) + 1
 else: 
    Number = int(input('Enter number'))