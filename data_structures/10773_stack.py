case = int(input())
stack = []
result = 0
for i in range(case):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
for j in stack:
    result += j
print(result)
