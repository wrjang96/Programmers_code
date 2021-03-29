def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        for i in range(2, n, 1):
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1000000007
        return arr[n-1]


print(solution(int(input())))