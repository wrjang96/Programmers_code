from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([[0,0]])
    while queue:
        temp, level = queue.popleft()
        if level > len(numbers):
            break
        elif temp == target and level == len(numbers):
            answer +=1
        if level < len(numbers):
             queue.append([temp + numbers[level], level + 1])
             queue.append([temp - numbers[level], level + 1])
    return answer


print(solution([1, 1, 1, 1, 1], 3))