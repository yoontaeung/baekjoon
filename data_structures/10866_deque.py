import sys
from collections import deque


if __name__ == '__main__':
    testcase = int(input())
    deq = deque()
    output = []
    for i in range(testcase):
        op = list(map(str, sys.stdin.readline().split()))
        if len(op) == 1:
            if op[0] == 'front':
                if len(deq) == 0:
                    output.append(-1)
                else:
                    output.append(deq[0])
            elif op[0] == 'back':
                if len(deq) == 0:
                    output.append(-1)
                else:
                    output.append(deq[len(deq)-1])
            elif op[0] == 'size':
                output.append(len(deq))
            elif op[0] == 'empty':
                if len(deq) == 0:
                    output.append(1)
                else:
                    output.append(0)
            elif op[0] == 'pop_front':
                if len(deq) == 0:
                    output.append(-1)
                else:
                    n = deq.popleft()
                    output.append(n)
            elif op[0] == 'pop_back':
                if len(deq) == 0:
                    output.append(-1)
                else:
                    n = deq.pop()
                    output.append(n)
        else:
            if op[0] == 'push_back':
                deq.append(int(op[1]))
            elif op[0] == 'push_front':
                deq.appendleft(int(op[1]))
    for j in range(len(output)):
        print(output[j])
