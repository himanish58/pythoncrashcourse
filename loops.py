# for and while loops

words = ['what', 'the', 'fuck', '!!!']
for a in words:
    print(a)

for i in range(len(words)):
    print(words[i])

for i in range(0, 20):
    print(i)

count = 0;
while count < 10:
    print('I love myself')
    if count == 7:
        break
    count = count+1