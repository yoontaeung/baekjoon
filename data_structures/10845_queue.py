case = int(input())
output = []
queue = []
for i in range(case):
    op = input().split()
    if op[0] == 'push':
        queue.append(op[1])
    elif op[0] == 'pop':
        if len(queue) == 0:
            output.append(-1)
        else:
            output.append(queue.pop(0))
    elif op[0] == 'size':
        output.append(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0:
            output.append(1)
        else:
            output.append(0)
    elif op[0] == 'front':
        if len(queue) == 0:
            output.append(-1)
        else:
            output.append(queue[0])
    elif op[0] == 'back':
        if len(queue) == 0:
            output.append(-1)
        else:
            output.append(queue[len(queue)-1])
for j in output:
    print(j)
