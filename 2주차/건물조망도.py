for test in range(1,11):
    BuildingCount = int(input())
    BuildingLength = list(map(int, input().split()))
    Result = 0
    for i in range(2, BuildingCount - 2):
        LengthMax = max(BuildingLength[i-2], BuildingLength[i-1], BuildingLength[i+1], BuildingLength[i+2])
        if BuildingLength[i] > LengthMax:
            Result += BuildingLength[i] - LengthMax

    print("#{}".format(test), Result)