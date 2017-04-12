# if, if-else, elif, nested if

num = 5
color = 'red'

if color == 'blue':
    print('color is blue')
elif color == 'green':
    print('color is green')
else:
    print('color is red')

if num < 9:
    if color == 'red':
        print('Number is less then 9 and color is red')

if num < 9 and color == 'red':
    print('Number is less then 9 and color is red')

if num < 5 or color == 'red':
    print('Either number is less then 5 or color is red')