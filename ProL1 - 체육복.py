def solution(n, lost, reserve):
    students = [1 for _ in range(n)]
    answer = 0
    for i in range(len(lost)):
        lost[i] -= 1
        students[lost[i]] -= 1
    for i in range(len(reserve)):
        reserve[i] -= 1
        students[reserve[i]] += 1
    for k in range(len(students)):
        if k == 0 and students[k] == 0:
            if students[k+1] == 2:
                students[k+1] = 1
                students[k] = 1
        elif k == len(students) -1 and students[k] == 0:
            if students[k-1] == 2:
                students[k-1] = 1
                students[k] = 1
        elif students[k] == 0:
            if students[k+1] == 2:
                students[k+1] = 1
                students[k] = 1
            elif students[k-1] == 2:
                students[k-1] = 1
                students[k] = 1
        answer = len(students) - students.count(0)
    return answer