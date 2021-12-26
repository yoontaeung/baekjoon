case = int(input())
output = []
for i in range(case):
    stack = []
    word = input().split()
    for j in range(len(word[0])):
        if word[0][j] == '(':
            stack.append('(')
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) > 0:
        output.append('NO')
    else:
        output.append('YES')
for j in output:
    print(j)
