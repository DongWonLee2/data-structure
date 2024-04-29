Test = 10

for i in range(1, Test+1):
    N, M = map(int, input("").split())
    Data = list(map(int, input("").split()))
    Total = []
    for j in range(N-M+1):
        current = 0
        for k in range(M):
            current += Data[j+k]
        Total.append(current)
    Result = max(Total) - min(Total)
    print("#{}".format(i), Result)     