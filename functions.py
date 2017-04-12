def test():
    print('Hello World')


test()


def addnum(num1, num2):
    a = num1 + num2
    return a

b = addnum(7, 9.5)
print('addnum = ', b)

def addnumber(num):
    num = num + 1
    print('inside the function num =', num)
    return
num = 5
addnumber(num)
print('outside the function num =', num)

def addlist(mylist):
    mylist.append('hi')
    print('value inside the function =', mylist)
    return
mylist = [1, 3, 5]
addlist(mylist)
print('value outside the function =', mylist)

