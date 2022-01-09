num = int(input())
arr = [0] * (num+1)

for i in range(2, num+1):
    temp = 10**6
    if arr[i] == 0:
        if i % 3 == 0:
            temp = min(temp, arr[i//3])
        if i % 2 == 0:
            temp = min(temp, arr[i//2])
        arr[i] = min(arr[i-1] + 1, temp + 1)
print(arr[num])
