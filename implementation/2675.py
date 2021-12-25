testcase = int(input())
for i in range(testcase):
    arr_list = list(map(str, input().split()))
    routine = int(arr_list[0])
    for j in range(len(arr_list[1])):
        for k in range(routine):
            print(arr_list[1][j], end='')
    print()
