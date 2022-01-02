def ppl(n: int, k: int) -> int:
    sum = 0
    if n == 0:
        return k
    else:
        for j in range(1, k+1):
            sum += ppl(n-1, j)
    return sum


if __name__ == '__main__':
    testcase = int(input())
    output = []
    for i in range(testcase):
        n = int(input())
        k = int(input())
        output.append(ppl(n, k))
    for j in range(len(output)):
        print(output[j])
