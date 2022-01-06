import sys

if __name__ == '__main__':
    n = int(input())
    card = sorted(map(int, sys.stdin.readline().split()))
    m = int(input())
    target = list(map(int, sys.stdin.readline().split()))

    d = dict()

    for i in card:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(m):
        if target[i] in d:
            print(d[target[i]], end=' ')
        else:
            print(0, end=' ')
