def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1
    graph = [[int(1e9)] * n for _ in range(n)]
    answer = 0
    for i in range(len(fares)):
        start = fares[i][0] - 1
        end = fares[i][1] - 1
        graph[start][end] = fares[i][2]
        graph[end][start] = fares[i][2]

    for i in range(n):
        graph[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = int(1e9)
    for i in range(n):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer



print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
