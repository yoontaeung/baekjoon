from collections import deque


if __name__ == '__main__':
    testcase = int(input())
    output = []
    docs = []
    for i in range(testcase):
        n, m = list(map(int, input().split()))
        docs = list(map(int, input().split()))
        deq = deque(docs)
        j = 0
        index = m
        cnt = 1
        while True:
            if deq[0] == max(deq) and index == 0:
                # printout
                output.append(cnt)
                break
            if deq[0] != max(deq):
                if index > 0:
                    deq.append(deq.popleft())
                    index -= 1
                else:
                    deq.append(deq.popleft())
                    index = len(deq) - 1
            else:
                cnt += 1
                deq.popleft()
                index -= 1
    for i in range(len(output)):
        print(output[i])
