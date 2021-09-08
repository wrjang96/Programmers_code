def solution(record):
    answer = []
    database = {}
    record.reverse()
    for ind_record in record:
        temp_str = ind_record.split()
        if temp_str[0] == 'Enter' or temp_str[0] == 'Change':
            if temp_str[1] in database:
                continue
            else:
                database[temp_str[1]] = temp_str[2]
    record.reverse()
    for ind_record in record:
        temp_str = ind_record.split()
        if temp_str[0] == 'Enter':
            ans_str = database[temp_str[1]]
            answer.append(ans_str + "님이 들어왔습니다.")
        elif temp_str[0] == 'Leave':
            ans_str = database[temp_str[1]]
            answer.append(ans_str + "님이 나갔습니다.")
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])