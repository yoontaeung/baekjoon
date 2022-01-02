if __name__ == '__main__':
    testcase = int(input())
    arr = []
    dict = {}
    _sum: int = 0
    for i in range(testcase):
        temp = int(input())
        arr.append(temp)
        _sum += temp
        if temp in dict:
            dict[temp] += 1
        else:
            dict[temp] = 1

    # find a mode
    m = (max(dict.values()))
    temp = []
    for key, value in dict.items():
        if value == m:
            temp.append(key)
    if len(temp) > 1:
        temp.sort()
        mode = temp[1]
    else:
        mode = temp[0]

    # find a mean
    mean = round(_sum/testcase)

    # find a medium
    arr.sort()
    medium = arr[(len(arr)-1)//2]

    # find a range
    _range = arr[len(arr)-1] - arr[0]

    print(mean)
    print(medium)
    print(mode)
    print(_range)
