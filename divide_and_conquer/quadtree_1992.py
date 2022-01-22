import sys
sys.setrecursionlimit(10000000)

n = int(input())
num = []
for i in range(n):
    num.append(sys.stdin.readline().rstrip())
output = []

def dnq(x, y, n):
    check = True
    temp = num[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num[i][j] != temp:
                output.append('(')
                check = False
                for k in range(2):
                    for l in range(2):
                        dnq(x + k*(n//2), y + l*(n//2), n//2)
                output.append(')')
                return
    if check:
        output.append(str(temp))

dnq(0, 0, n)
for i in output:
    print(i, end='')
