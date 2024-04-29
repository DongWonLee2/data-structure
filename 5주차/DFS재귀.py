def DFS(here):
    visited[here] = True
    print(here)
    for next in range(1, howmany + 1):
        if not visited[next] and MyMap[here][next]:
            DFS(next)

howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]
visited = [0] * (howmany + 1)

for i in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1
DFS(1)