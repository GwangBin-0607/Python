def solution(n,k):
    p = n // 10
    pp = k - p
    return (n*12000)+(pp*2000)
print(solution(64,6))
