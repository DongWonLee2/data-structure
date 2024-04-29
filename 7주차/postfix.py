isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}
icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 3}

Data = '1+2*3+(4+5)/61'
stack = []
postFix = []
for now in Data:
    if '0' <= now <= '9':
        postFix += [now]
    elif now == ')':
        while stack[-1] != '(':
            postFix+=[stack.pop()]
        stack.pop()
    else:
        if not stack:
            stack += [now]
        elif icp[now] > isp[stack[-1]]:
            stack += [now]
        else:
            while stack and isp[stack[-1]] >= icp[now]:
                postFix += [stack.pop()]
            stack += [now]
while stack:
    postFix += [stack.pop()]
print(postFix)