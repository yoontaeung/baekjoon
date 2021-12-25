arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
# to get rid of duplicate elements
arr = set(arr)
print(len(arr))
