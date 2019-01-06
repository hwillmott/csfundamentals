import string
f = open('./alice-in-wonderland.txt', 'r')
s = f.read()
lowercase = s.lower()
withoutpunch = lowercase.translate(string.punctuation)
words = withoutpunch.split()
stringD = dict()
for string in words:
    if string in stringD:
        stringD[string] = stringD[string] + 1
    else:
        stringD[string] = 1
listD = []
for key, value in stringD.items():
    temp = [key, value]
    listD.append(temp)
sortedD = sorted(listD, key=lambda x: x[1], reverse=True)
for i in range(10):
    print(sortedD[i][0])

f.close()
