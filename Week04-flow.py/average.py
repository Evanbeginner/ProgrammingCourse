numbers = []


number = int(input('enter number ( 0 to quit)'))

while number != 0:
    numbers.append(number)
    number = int(input('enter number ( o to quit)'))

averagenumber = (sum(numbers)/ len(numbers))
print(averagenumber)

