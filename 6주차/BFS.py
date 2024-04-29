def BFS():
    while myQueue:
        here = myQueue.pop(0)
        Visited[here] = True
        print(here)
        for next in range(1, howmany+1):
            if not Visited[next] and MyMap[here][next]:
                Visited[next] = True
                myQueue.append(next)

howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]
Visited = [0] * (howmany+1)
myQueue = []


for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

myQueue.append(1)
BFS()


