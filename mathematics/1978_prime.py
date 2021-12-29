def find(n:int) -> int:
    if n == 1:
        return 0
    else:
        m = int(n/2)
        temp = 0
        for i in range(1, m+1):
            if n % i == 0:
                temp += 1
            if temp == 2:
                return 0
        return 1


if __name__ == '__main__':
    case = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    for i in range(case):
        j = find(num[i])
        cnt += j
    print(cnt)
