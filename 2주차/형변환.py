# atoi
Data = ['1', '2', '3']
val = 0
for i in range(len(Data)):
    val = val * 10 + int((Data[i]))
print(val)

# itoa
val = 123
temp = val
howmany = 0

while temp:
    howmany += 1
    temp //= 10

Data = [0] * howmany

for i in range(howmany-1, -1, -1):
    Data[i] = str(val%10)
    val //= 10

'''
while howmany:
howmany -= 1
Data[howmany] = str(val%10)
val //= 10
'''
print(Data)

#another
val = 123
temp =str(val) 
Data = [0, 0, 0]
for i, j in enumerate(temp):
    Data[i] = j
print(Data)