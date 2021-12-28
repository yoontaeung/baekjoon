if __name__ == '__main__':
    num = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    result = 0
    for i in range(len(arr)):
        count += arr[i]
        result += count
    print(result)
