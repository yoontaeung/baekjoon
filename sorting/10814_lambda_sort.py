import sys

if __name__ == '__main__':
    testcase = int(input())
    output = []
    t = []
    for i in range(testcase):
        age, name = map(str, input().split())
        age = int(age)
        t.append((age, name))

    t.sort(key = lambda x: x[0])
    for i in t:
        print(i[0], i[1])

