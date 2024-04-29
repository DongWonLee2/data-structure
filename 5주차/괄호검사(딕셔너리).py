pare = {'>':'<', ')':'(', '}':'{', ']':'['}
Data = ['<', '(', ')', '>', '(', '>']
stack = []
ans = 0
isCorrect = True

while Data:
    now = Data.pop(0)
    if now in pare.values():
        stack.append(now)
    elif stack and stack[-1] == pare[now]:
        stack.pop()
    else:
        isCorrect = False
        break
if not stack and isCorrect:
    ans = 1
print(ans)