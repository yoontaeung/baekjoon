word = input()
arr = []
for i in range(26):
    arr.append(0)
for j in word:
    if ord(j) < 97:
        arr[ord(j) - 65] += 1
    else:
        arr[ord(j) - 97] += 1
m = max(arr)
arr2 = ([index for index, item in enumerate(arr) if item == m])
if len(arr2) == 1:
    print(chr(arr2[0]+65))
else:
    print('?')
