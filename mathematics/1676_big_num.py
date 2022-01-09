num = int(input())

# arr[i] 는 i! 의 0의 개수를 담고 있다
arr = [0]*(num+1)
temp = 4

for i in range(5, num+1):
    arr[i] = arr[i-1]
    temp *= i

    temp_str = str(temp)
    j = len(temp_str) - 1
    while temp_str[j] == '0':
        arr[i] += 1
        j -= 1
    if i >= 10:
        temp = int(temp_str[j]) + int(temp_str[j-1])*10
    elif i >= 100:
        temp = int(temp_str[j]) + int(temp_str[j-1])*10 + int(temp_str[j-2])*100
    else:
        temp = int(temp_str[j])

print(arr[num])
