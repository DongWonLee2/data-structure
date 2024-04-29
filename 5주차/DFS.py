def dfs(start):
    stack.append(start)  
    while stack:
        v = stack.pop()  
        if not visited[v]:
            visited[v] = True  
            print(v, end=' ')  
            for i in range(len(MyMap[v]) - 1, -1, -1):
                if MyMap[v][i] and not visited[i]:
                    stack.append(i)

howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]
visited = [0] * (howmany + 1)
stack = []

for i in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

dfs(1)