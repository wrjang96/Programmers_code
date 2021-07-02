def solution(strings, n):
    temp_arr =[]
    answer = []
    for i in range(len(strings)):
        temp_arr.append([strings[i][n], strings[i]])
    temp_arr.sort()
    for i in range(len(strings)):
        answer.append(temp_arr[i][1])
    return answer