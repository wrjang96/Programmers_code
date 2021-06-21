Fibo = [-1 for i in range(100001)]
Fibo[0] = 0
Fibo[1] = 1
def solution(n):
    for i in range(2, n+1, 1):
        Fibo[i] = ((Fibo[i-1]% 1234567) + (Fibo[i-2]% 1234567) )% 1234567
    return Fibo[n]