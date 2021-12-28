if __name__ == '__main__':
    n = int(input())

    i = 0
    m = 2
    while True:
        if n == 1:
            i = -1
            break
        else:
            if m <= n < m + 6*(i+1):
                break
            else:
                m = m + 6 * (i + 1)
                i += 1
    print(i+2)
