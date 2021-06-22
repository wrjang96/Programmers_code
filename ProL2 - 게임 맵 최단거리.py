dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = [[0,0,1]]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for i in range(n)]
    visited[0][0] = 1
    answer = -1
    while(queue):
        x, y, cnt = queue.pop(0)
        print(x, y, cnt)
        if x == n - 1 and y == m - 1:
            answer = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny, cnt + 1])
    return answer

print(solution([[1, 0, 1, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 1, 0], [0, 0, 0, 1]]))
