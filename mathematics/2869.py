if __name__ == '__main__':
    a, b, v = list(map(int, sys.stdin.readline().split()))
    if a == v:
        days = 1
    else:
        if (v-a) % (a-b) == 0:
            days = (v-a)//(a-b) + 1
        else:
            days = (v-a)//(a-b) + 2
    print(days)
