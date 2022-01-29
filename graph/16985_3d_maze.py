import sys
from collections import deque
import copy
from itertools import permutations
maze = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(7)]
real_result = []
# 7x7x7 maze
for i in range(5):
    for j in range(5):
        t = list(map(int, sys.stdin.readline().split(' ')))
        for k in range(5):
            if t[k] == 1:
                maze[i+1][j+1][k+1] = 1


def rotate_two(layer):
    result_layer = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(1, 6):
        for j in range(1, 6):
            result_layer[j][6-i] = layer[i][j]
    return result_layer


def find_way(graph, x_cord, y_cord, z_cord):
    if graph[x_cord][y_cord][z_cord] == 0:
        return -1
    visited = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(7)]
    dist = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(7)]
    x_queue = deque()
    y_queue = deque()
    z_queue = deque()
    visited[x_cord][y_cord][z_cord] = 1
    x_queue.append(x_cord)
    y_queue.append(y_cord)
    z_queue.append(z_cord)
    while len(x_queue) != 0:
        x = x_queue.popleft()
        y = y_queue.popleft()
        z = z_queue.popleft()
        if x == (6-x_cord) and y == (6-y_cord) and z == (6-z_cord):
            #print(dist[x][y][z])
            return dist[x][y][z]
        if graph[x+1][y][z] == 1:
            if visited[x+1][y][z] == 0:
                visited[x+1][y][z] = 1
                x_queue.append(x+1)
                y_queue.append(y)
                z_queue.append(z)
                dist[x+1][y][z] = dist[x][y][z] + 1
        if graph[x][y+1][z] == 1:
            if visited[x][y+1][z] == 0:
                visited[x][y+1][z] = 1
                x_queue.append(x)
                y_queue.append(y+1)
                z_queue.append(z)
                dist[x][y+1][z] = dist[x][y][z] + 1
        if graph[x][y][z+1] == 1:
            if visited[x][y][z+1] == 0:
                visited[x][y][z+1] = 1
                x_queue.append(x)
                y_queue.append(y)
                z_queue.append(z+1)
                dist[x][y][z+1] = dist[x][y][z] + 1
        if graph[x][y][z-1] == 1:
            if visited[x][y][z-1] == 0:
                visited[x][y][z-1] = 1
                x_queue.append(x)
                y_queue.append(y)
                z_queue.append(z-1)
                dist[x][y][z-1] = dist[x][y][z] + 1
        if graph[x][y-1][z] == 1:
            if visited[x][y-1][z] == 0:
                visited[x][y-1][z] = 1
                x_queue.append(x)
                y_queue.append(y-1)
                z_queue.append(z)
                dist[x][y-1][z] = dist[x][y][z] + 1
        if graph[x-1][y][z] == 1:
            if visited[x-1][y][z] == 0:
                visited[x-1][y][z] = 1
                x_queue.append(x-1)
                y_queue.append(y)
                z_queue.append(z)
                dist[x-1][y][z] = dist[x][y][z] + 1
    return -1


def rotate(maze_x, a, b, c, d, e):
    temp_maze = copy.deepcopy(maze_x)

    for _ in range(a):
        temp_maze[1] = rotate_two(temp_maze[1])

    for _ in range(b):
        temp_maze[2] = rotate_two(temp_maze[2])

    for _ in range(c):
        temp_maze[3] = rotate_two(temp_maze[3])

    for _ in range(d):
        temp_maze[4] = rotate_two(temp_maze[4])

    for _ in range(e):
        temp_maze[5] = rotate_two(temp_maze[5])
    return temp_maze


iterator = [1,2,3,4,5]
maze_xx = copy.deepcopy(maze)
arr = [1, 5]

def sol2():
    for floor in permutations(iterator, 5):
        for p in range(1, 6):
            maze_xx[p] = maze[floor[p-1]]
        for jj in range(2):
            for kk in range(2):
                if maze_xx[1][arr[jj]][arr[kk]] == 1:
                    rr = find_way(maze_xx, 1, arr[jj], arr[kk])
                    if rr != -1:
                        if rr == 12:
                            real_result.append(rr)
                            return
                        else:
                            real_result.append(rr)
        if len(real_result) == 0:
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        for l in range(4):
                            for w in range(4):
                                r = rotate(maze_xx, i, j, k, l, w)
                                for jj in range(2):
                                    for kk in range(2):
                                        if r[1][arr[jj]][arr[kk]] == 1:
                                            rr = find_way(r, 1, arr[jj], arr[kk])
                                            if rr != -1:
                                                if rr == 12:
                                                    real_result.append(rr)
                                                    return
                                                else:
                                                    real_result.append(rr)
# def sol():
#     for floor in permutations(iterator, 5):
#         for p in range(1, 6):
#             maze_xx[p] = maze[floor[p-1]]
#         for i in range(4):
#             for j in range(4):
#                 for k in range(4):
#                     for l in range(4):
#                         for w in range(4):
#                             r = rotate(maze_xx, i, j, k, l, w)
#                             for jj in range(2):
#                                 for kk in range(2):
#                                     if r[1][arr[jj]][arr[kk]] == 1:
#                                         rr = find_way(r, 1, arr[jj], arr[kk])
#                                         if rr != -1:
#                                             if rr == 12:
#                                                 real_result.append(rr)
#                                                 return
#                                             else:
#                                                 real_result.append(rr)


sol2()
if len(real_result) == 0:
    print(-1)
else:
    print(min(real_result))
