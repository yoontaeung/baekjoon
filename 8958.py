testcase = int(input())

for i in range(testcase):
    result: int = 0
    score = input()
    sub_score: int = 1
    for j in range(len(score)):
        if score[j] == 'O':
            result += sub_score
            sub_score += 1
        else:
            sub_score = 1
    print(result)
