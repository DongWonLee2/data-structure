howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]

for i in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

for j in MyMap:
    print(j)