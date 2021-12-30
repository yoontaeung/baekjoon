if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    set1 = set()
    set2 = set()
    if m == 1:
        set1.add(1)
    else:
        for i in range(1, m+1):
            if m % i == 0:
                set1.add(i)
    if n == 1:
        set2.add(1)
    else:
        for j in range(1, n+1):
            if n % j == 0:
                set2.add(j)
    w = max(set1 & set2)

    print(w)
    print(w*(m//w)*(n//w))
    
    # 유클리드 호제법으로 푸는 것은 아래와 같음. 
    """ 
    def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    """
    # 이외에도 math 라이브러리를 사용해 gcd, lcm 바로 구하는 함수가 존재
