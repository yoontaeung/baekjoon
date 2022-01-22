import sys
sys.setrecursionlimit(10000000)

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

minus_one = 0
plus_one = 0
zero = 0

def dnq(x, y, n):
    global minus_one, plus_one, zero
    temp = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != temp:
                for k in range(3):
                    for l in range(3):
                        dnq(x + (n//3)*(k), y + (n//3)*(l), n//3)
                return
    if temp == -1:
        minus_one += 1
    elif temp == 0:
        zero += 1
    else:
        plus_one += 1
dnq(0, 0, n)
print(minus_one, zero, plus_one)
