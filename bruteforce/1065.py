num = int(input())
result = 99
if num < 100:
    print(num)
else:
    for i in range(100, num+1):
        s = str(i)
        if (int(s[0]) - int(s[1])) == (int(s[1]) - int(s[2])):
            result += 1
    print(result)
