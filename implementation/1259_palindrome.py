if __name__ == '__main__':
    output = []
    while True:
        num = input()
        if int(num) == 0:
            break
        else:
            check = True
            for i in range(len(num)):
                if num[i] != num[len(num) - i - 1]:
                    check = False
                    break
            if check:
                output.append('yes')
            else:
                output.append('no')
    for j in range(len(output)):
        print(output[j])
