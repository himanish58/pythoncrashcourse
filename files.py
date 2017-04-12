# Open a file

fo = open('test.txt', 'w')

# get some info

print('File Name:', fo.name)
print('Colsed? :', fo.closed)
print('Mode:', fo.mode)

# write

fo.write('I love python')
fo.write(' and Javascript')
fo.close()

# write to append

fo = open('test.txt', 'a')
fo.write(' and I want to be a full stack developer')
fo.close()

# read from file

fo = open('test.txt', 'r+')
text = fo.read(19)
print(text)
fo.close()

# create file

fo = open('test1.txt', 'w+')
fo.write('python is cool')
fo.close()