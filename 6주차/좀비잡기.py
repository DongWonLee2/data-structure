
def bfs():
    while queue:
        here = queue.pop(0)
        for i in range(3):
            next = here + move[i]
            if next > len(time) - 1:
                continue
            if time[next] > time[here] + 1:
                time[next] = time[here] + 1
                queue.append(next)

sLL, zombie = map(int, input().split())
move = [0] * 3
move[0], move[1], move[2] = map(int, input().split())

queue = []
time = [987654321] * 1000
time[sLL] = 0
queue.append(sLL)

bfs()

if (time[zombie] != 987654321 ):
    print(time[zombie])
else:
    print(-1)