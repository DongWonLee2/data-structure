def bfs(start):
    queue.append(start)
    distance[start] = 0
    while queue:
        here = queue.pop(0)
        for next in myMap[here]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[here] + 1

howmany, start = map(int, input().split())
Data = list(map(int, input().split()))
myMap = [[] for i in range(101)]
queue = []

for i in range(0, len(Data), 2):
    _from, _to = Data[i], Data[i+1]
    myMap[_from].append(_to)

distance = [-1] * 101

bfs(start)
max = distance[0]

for i in range(len(distance)):
    if distance[i] >= max:
        max = distance[i]
        ans = i

print(ans)