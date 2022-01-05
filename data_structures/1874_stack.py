import sys

if __name__ == '__main__':
    stack = []
    output = []
    arr = []
    testcase = int(input())
    for i in range(testcase):
        arr.append(int(input()))
    j = 0
    i = 1
    while True:
        if len(stack) == 0:
            stack.append(i)
            output.append('+')
            i += 1

        if stack[-1] == arr[j]:
            stack.pop()
            output.append('-')
            j += 1
        elif stack[-1] < arr[j]:
            stack.append(i)
            output.append('+')
            i += 1
        else:
            print('NO')
            break
        if j == testcase:
            for k in range(len(output)):
                print(output[k])
            break
