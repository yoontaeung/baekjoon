testcase = int(input())
result_list = []
result = 0
score_list = list(map(int, input().split()))
max_value = max(score_list)
for j in range(len(score_list)):
    result_list.append(score_list[j]/max_value*100)
    result += result_list[j]

print(result/len(score_list))
