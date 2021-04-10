with open('count.txt', 'w') as f:
    f.write('0')

file = 'count.txt'

def readfile():
    with open(file, 'w') as f:
        f.write('overwrite')
      


print(readfile())


def writefile(number):
    with open(file,'wt') as f:
        f.write(str(number))


writefile(1)