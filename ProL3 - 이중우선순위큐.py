def solution(operations):
    temp = []
    answer = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            temp.append(int(operations[i][2:len(operations[i])]))
        elif operations[i][0] == 'D' and len(temp) != 0:
            if operations[i][2] == '1':
                temp.remove(max(temp))
            elif operations[i][2] == '-' and operations[i][3] == '1':
                temp.remove(min(temp))

    if len(temp) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(temp))
        answer.append(min(temp))
    return answer