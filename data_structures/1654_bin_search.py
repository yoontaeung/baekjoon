import sys

if __name__ == '__main__':
    k, n = list(map(int, sys.stdin.readline().split()))
    arr = []
    for i in range(k):
        arr.append(int(sys.stdin.readline()))
    left = 1
    right = max(arr)
    while left <= right:
        mid = (left+right)//2
        sum = 0
        for i in range(k):
            sum += arr[i]//mid
        if sum < n:
            right = mid - 1
        else:
            left = mid + 1
    print(right)
