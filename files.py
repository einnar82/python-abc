# writing files in python
myFile = open('sample.txt', 'w')

myFile.write('python WTF')
myFile.close()

# append to file
appendFile = open('sample.txt', 'a')
appendFile.write(' Yess sir')
appendFile.close()

# read a file
readFile = open('sample.txt', 'r+')
txt = readFile.read(100)
print(txt)
