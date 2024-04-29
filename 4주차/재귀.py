ans = 0
digit = 1
def GetSome(num):
    global ans
    global digit
    if num > 0:
        GetSome(int(num / 10))
        ans += (num % 10) * digit
        digit *= 10
    return

GetSome(321)
print(ans)

Data = [1, 6, 5, 4, 3, 2]
howmany = len(Data)

def solve(now):
    while now < howmany - 1:
        where = Data.index(min(Data[now : howmany]))
        Data[now], Data[where] = Data[where], Data[now]
        now += 1
solve(0)
print(Data)

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)