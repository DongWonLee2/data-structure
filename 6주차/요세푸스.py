Queue = []
people = 41
for i in range(1, people+1):
    Queue.append(i)
while len(Queue) != 3:
    alive1 = Queue.pop(0)
    alive2 = Queue.pop(0)
    dead = Queue.pop(0)
    Queue.append(alive1)
    Queue.append(alive2)
print(Queue.pop(0), Queue.pop(0), Queue.pop(0))

'''
Queue = []
people = 41
for i in range(1, people+1):
    Queue.append(i)
while len(Queue) != 3:
    Queue.append(Queue.pop(0))
    Queue.append(Queue.pop(0))
    dead = Queue.pop(0)
print(Queue.pop(0), Queue.pop(0), Queue.pop(0))
'''

# N, K = map(int, input().split())
# Queue = []
# result = []
# for i in range(1, N + 1):
#     Queue.append(i)

# print('<', end = '')
# while len(Queue)>1:
#     for j in range(K-1):
#         Queue.append(Queue.pop(0))
#     print(Queue.pop(0), end = ', ')

# print(Queue.pop(0), end = '')
# print('>')