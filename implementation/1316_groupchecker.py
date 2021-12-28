if __name__ == '__main__':
    num = int(input())
    result = 0
    for i in range(num):
        arr = []
        word = input()
        check = True
        for j in range(len(word)):
            if word[j] not in arr:
                arr.append(word[j])
            else:
                if word[j-1] != word[j]:
                    check = False
        if check:
            result += 1
    print(result)
