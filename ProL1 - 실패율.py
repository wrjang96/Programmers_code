def solution(N, stages):
    answer = []
    arr = [[0, 0] for _ in range(N + 2)]
    answer_arr = []
    for stage in stages:
        for i in range(1, stage + 1):
            arr[i][0] += 1
            if i == stage:
                arr[i][1] += 1

    for i in range(1, N + 1):
        if arr[i][1] == 0 or arr[i][0] == 0:
            answer_arr.append([0, i])
        else:
            answer_arr.append([- arr[i][1] / arr[i][0], i])
    answer_arr.sort()
    for i in range(len(answer_arr)):
        answer.append(answer_arr[i][1])

    return answer