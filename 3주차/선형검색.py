Data = [6, 4, 3, 2, 1, 9, 8]
key = 5

for i in range(len(Data)):
    if key == Data[i]:
        print("find out")
        break
else:
    print("no data")