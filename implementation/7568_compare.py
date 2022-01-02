if __name__ == '__main__':
    n = int(input())
    height = []
    weight = []
    output = []
    for i in range(n):
        h, w = list(map(int, input().split()))
        height.append(h)
        weight.append(w)
    cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if height[i] < height[j]:
                if weight[i] < weight[j]:
                    cnt += 1
        output.append(cnt+1)
    for i in range(len(output)):
        print(output[i], end=' ')

