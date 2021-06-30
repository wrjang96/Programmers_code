from itertools import permutations
import math

def solution(numbers):
    array = [True for i in range(0, 9999999 + 2, 1)]
    visited = [False for i in range(0, 9999999 + 2, 1)]
    combinations_list = []
    cnt = 0
    for i in range(2, int(math.sqrt(9999999 + 1)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= 9999999 + 1:
                array[i * j] = False
                j += 1
    array[0] = False
    array[1] = False
    for j in range(1, len(numbers) + 1, 1):
        combinations_list.append(list(map(''.join, permutations(numbers, j))))
    for i in range(len(combinations_list)):
        for j in range(len(combinations_list[i])):
            if visited[int(combinations_list[i][j])] == False and array[int(combinations_list[i][j])] == True:
                cnt += 1
            visited[int(combinations_list[i][j])] = True
    return cnt
