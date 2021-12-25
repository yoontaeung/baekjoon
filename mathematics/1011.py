testcase = int(input())
arr = []
"""
피라미드형식으로 거리가 더해지는 경우는 떨어진 거리가 제곱수인 경우임
예를 들어 9와 16 사이 그 절반인 12, 13을 기준으로 필요한 이동거리 횟수가 달라짐
j는 해당 dist가 어느 제곱수 사이에 위치하는지 파악함
"""
for i in range(testcase):
    arr = input().split()
    dist = int(arr[1]) - int(arr[0])
    j = 1
    while dist > (j**2):
        j += 1
    temp = (j**2) - (j-1)**2 - 1
    if dist <= ((j-1)**2 + temp/2):
        print(2*j-2)
    else:
        print(2*j-1)
