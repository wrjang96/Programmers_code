from collections import deque
queue = deque([])
def solution(n, computers):
    network_num = 0
    visited = [0 for _ in range(n)]
    for _ in range(n):
        if visited[_] == 0:
            queue.append(_)
            network_num += 1
        while queue:
            temp = queue.popleft()
            visited[temp] = 1
            for i in range(n):
                if i != temp:
                    if computers[i][temp] == 1 and visited[i] == 0:
                        visited[i] = temp
                        queue.append(i)

    answer = network_num
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])