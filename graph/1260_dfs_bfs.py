from collections import deque

def bfs(v):
    found = [v]
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and (i not in found):
                found.append(i)
                queue.append(i)

def dfs(v, found = []):
    found.append(v)
    print(v, end = ' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and (i not in found):
            dfs(i, found)





if __name__ == '__main__':
    n, m, v = list(map(int, input().split()))
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        m1, m2 = map(int, input().split())
        graph[m1][m2] = graph[m2][m1] = 1
    dfs(v)
    print()
    bfs(v)

