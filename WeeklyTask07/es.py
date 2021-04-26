import os
import requests

filename = str(input('Enter file'))



if (os.path.exists(filename)):
   with open(filename,'r') as f:
       data = f.read()
       count = 0
       for char in data:
           if char == 'e':
               count +=1
       print(count)      



         
else:
    with open(filename,"x") as f:
        print("creating the file")

