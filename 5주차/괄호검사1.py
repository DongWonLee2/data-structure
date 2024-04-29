for i in range(1, 4):
    print("# %d" %i, end = " ")
    stack = []
    Data = input()
    howmany = len(Data)
    isCorrect = True
    for j in range(howmany):
        if Data[j] == '(':
            stack.append(Data[j])
        else:
            if not stack or stack[-1] != '(':
                isCorrect = False
                break
            else:
                stack.pop()
    if not stack and isCorrect:
        print("CORRECT")
    else:
        print("WRONG")