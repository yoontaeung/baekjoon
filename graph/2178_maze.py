import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
temp = []
maze = [[0]*(m+2) for _ in range(n+2)]

for _ in range(n):
    temp.append(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(m):
        if temp[i][j] == '1':
            maze[i+1][j+1] = 1

visited = [[0]*(m+2) for _ in range(n+2)]  # 0 - unvisited, 1 - visited
dist = [[0]*(m+2) for _ in range(n+2)]
dist[1][1] = 1

def bfs(graph, x_cord, y_cord):
    x_queue = deque()
    y_queue = deque()
    visited[x_cord][y_cord] = 1
    x_queue.append(x_cord)
    y_queue.append(y_cord)
    while len(x_queue) != 0 and len(y_queue) != 0:
        x = x_queue.popleft()
        y = y_queue.popleft()
        if x == n and y == m:
            print(dist[x][y])
            break
        if maze[x+1][y] == 1:
            if visited[x+1][y] == 0:
                visited[x+1][y] = 1
                x_queue.append(x+1)
                y_queue.append(y)
                dist[x+1][y] = dist[x][y] + 1
        if maze[x-1][y] == 1:
            if visited[x-1][y] == 0:
                visited[x-1][y] = 1
                x_queue.append(x-1)
                y_queue.append(y)
                dist[x-1][y] = dist[x][y] + 1
        if maze[x][y+1] == 1:
            if visited[x][y+1] == 0:
                visited[x][y+1] = 1
                x_queue.append(x)
                y_queue.append(y+1)
                dist[x][y+1] = dist[x][y] + 1
        if maze[x][y-1] == 1:
            if visited[x][y-1] == 0:
                visited[x][y-1] = 1
                x_queue.append(x)
                y_queue.append(y-1)
                dist[x][y-1] = dist[x][y] + 1
    return


bfs(maze, 1, 1)


