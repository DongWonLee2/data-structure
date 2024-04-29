start, end = map(int, input().split())

for i in range(start, end+1):
    bl = True
    for div in range(2, i // 2 + 1):
        if(i % div) == 0:
            bl = False
    if bl:
        print(i)

import math
start, end = map(int, input().split())

for i in range(start, end+1):
    bl = True
    #for div in range(2, i // 2 + 1):
    for div in range(2, int(math.sqrt(i)+1)):
        if(i % div) == 0:
            bl = False
    if bl:
        print(i)