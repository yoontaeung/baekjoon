# 생성자를 모두 고르고 1-10000에서 빼서 답을 구함

arr = []
output = []
for i in range(1, 10):
    s = str(i)
    r = i + int(s[0])
    arr.append(r)
for j in range(10, 100):
    s = str(j)
    r = j + int(s[0]) + int(s[1])
    arr.append(r)
for k in range(100, 1000):
    s = str(k)
    r = k + int(s[0]) + int(s[1]) + int(s[2])
    arr.append(r)
for l in range(1000, 10000):
    s = str(l)
    r = l + int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
    arr.append(r)
arr.append(10000)
arr.sort()
for m in range(1, 10001):
    if m not in arr:
        output.append(m)
for n in output:
    print(n)
