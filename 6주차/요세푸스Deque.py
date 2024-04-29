from collections import deque
N, K = map(int, input().split())
Queue = deque(list(range(1, N + 1)))
print('<', end = '')
while len(Queue)>1:
    for j in range(K-1):
        Queue.append(Queue.popleft())
    print(Queue.popleft(), end = ', ')

print(Queue.popleft(), end = '')
print('>')