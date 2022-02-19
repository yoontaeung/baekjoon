import sys

n, m, k = map(int, input().split())  

parents = []
for _ in range(n+1):
    parents.append(_) 

def find(x):
    if x != parents[x]:
        parents[x]  = find(parents[x])
        return parents[x]
    else:
        return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if cost[x] < cost[y]:
            parents[y] = x
        else:
            parents[x] = y

cost = [0] + list(map(int, sys.stdin.readline().split()))   # 1번 인덱스에 1번 친구
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)
res = 0
for idx,root in enumerate(parents):
    if idx ==root:
        res+=cost[idx]

if res<=k:
    print(res)
else:
    print("Oh no")
