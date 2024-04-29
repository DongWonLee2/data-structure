num = int(input())
Data = [i for i in range(num)]

for i in range(num//2):
    Data[i], Data[num-1-i] = Data[num-1-i], Data[i]

print(Data)

'''
list00 = [i for i in range(1, 7)]
dummylist = list00[3:6]
dummylist.reverse()
list00[3:6] = dummylist
print(dummylist)
print(list00)
'''