def binarySearch2( low, high, key) :
    if low > high : # �˻� ����
        return False
    else :
        middle = (low + high) // 2
        if key == Data[middle] : # �˻� ����
            return True
        elif key < Data[middle] :
            return binarySearch2( low, middle-1, key)
        elif Data[middle] < key :
            return binarySearch2( middle+1, high, key)
Data = list(map(int, input().split()))
Data.sort()
howmany = len(Data)
key  = 11
print(binarySearch2( 0, howmany-1, key))
print(Data)
