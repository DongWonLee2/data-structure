def BFS():
    while myQueue:
        here = myQueue.pop(0)
        Visited[here] = True
        print(here)
        for next in range(1, howmany+1):
            if not Visited[next] and MyMap[here][next]:
                Parent[next] = here
                Distance[next] = Distance[here] + 1
                Visited[next] = True
                myQueue.append(next)
howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]
Visited = [0] * (howmany+1)
myQueue = []
Parent = [0] * (howmany+1)
Distance = [0] * (howmany+1)
for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1
myQueue.append(1)
Parent[1] = -1
Distance[1]=1
BFS()
print(Distance)
print(Parent)
