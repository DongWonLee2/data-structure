Data = [2,4,7,9,11,19,23]
N = 9
start = 0
end  = len(Data)
cnt = 1

while start <= end:
    find = (start + end) // 2
    if Data[find] == N:
        print("{},검색완료".format(cnt))
        break
    elif Data[find] > N:
        end = find
    else:
        start = find
    cnt += 1