if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        m1, m2 = map(int, input().split())
        graph[m1][m2] = graph[m2][m1] = 1
    count = 0
    found = []
    stack = []
    stack.append(1)
    found.append(1)
    while stack:
        w = stack.pop()
        for i in range(len(graph[w])):
            if graph[w][i] == 1 and (i not in found):
                stack.append(i)
                found.append(i)
                count += 1

    print(count)
