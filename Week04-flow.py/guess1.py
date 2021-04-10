correctnumber = 7

GuessNumber = int(input('Guess the number'))

while GuessNumber != correctnumber:
    if GuessNumber < correctnumber:
     print('Very close too low!')
     GuessNumber = int(input('Guess the number'))
    else :
     print('Too High')
     GuessNumber = int(input('Guess the number'))

print('Correct! the number was {}'.format(correctnumber))