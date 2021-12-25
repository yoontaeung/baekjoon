testcase = int(input())
score = []

for i in range(testcase):
    result = 0
    output = 0

    score = list(map(int, input().split()))
    students = score[0]
    for j in range(1, len(score)):
        result += score[j]
    mean = result/students
    for k in range(1, len(score)):
        if score[k] > mean:
            output += 1
    print("{:.3f}%".format(round(output/students*100, 3)))
