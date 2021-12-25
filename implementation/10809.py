a = input()
arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
num: int = 0
for i in a:
    if arr[ord(i) - 97] == -1:
        arr[ord(i) - 97] = num
    num += 1
for j in arr:
    print(j, end=' ')

