case = int(input())

print_list = []
stack = []
for i in range(case):
    op = input().split()
    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'top':
        if len(stack) == 0:
            print_list.append(-1)
        else:
            print_list.append(stack[-1])
    elif op[0] == 'size':
        print_list.append(len(stack))
    elif op[0] == 'empty':
        if len(stack) == 0:
            print_list.append(1)
        else:
            print_list.append(0)
    elif op[0] == 'pop':
        if len(stack) == 0:
            print_list.append(-1)
        else:
            print_list.append(stack.pop())

for j in print_list:
    print(j)
