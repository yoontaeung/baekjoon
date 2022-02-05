import sys
n = int(input())
ground = []
temp = 10000000

for _ in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))

direction = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[False]*n for _ in range(n)]


def check(x, y):
    global n
    for dx, dy in direction:
        _x = x + dx
        _y = y + dy
        if _x < 0 or _y < 0 or _x > n-1 or _y > n-1 or visited[_x][_y]:
            return False
    return True


def cal(x, y):
    global n
    res = 0
    for dx, dy in direction:
        _x = x + dx
        _y = y + dy
        res += ground[_x][_y]
    return res


def find(x, cost, cnt):
    global temp
    if cnt == 3:
        temp = min(cost, temp)
        return
    for i in range(x, n):
        for j in range(1, n):
            if check(i, j):
                visited[i][j] = True
                for dx, dy in direction:
                    visited[i+dx][j+dy] = True
                find(i, cost + cal(i, j), cnt+1)
                visited[i][j] = False
                for dx, dy in direction:
                    visited[i+dx][j+dy] = False
find(1, 0, 0)
print(temp)
