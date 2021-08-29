from collections import deque

def solution(new_id):
    answer =''
    new_temp = ''
    for i in range(len(new_id)):
        if ord(new_id[i]) >= 65 and ord(new_id[i])<=90:
            new_temp += chr(ord(new_id[i]) + 32)
        elif ord(new_id[i]) == 45 or ord(new_id[i]) == 95 or ord(new_id[i]) >= 97 and ord(new_id[i])<=122 or ord(new_id[i]) >= 48 and ord(new_id[i])<= 57 or ord(new_id[i]) == 46:
            new_temp += new_id[i]
    print(new_temp)
    temp_str = ''
    temp =''
    for i in range(len(new_temp)):
        if ord(new_temp[i]) == 46:
            if i + 1 <= len(new_temp)-1 and ord(new_temp[i + 1]) == 46:
                continue
            else:
                temp_str += new_temp[i]
        else:
            temp_str += new_temp[i]
    temp = temp_str
    while temp != "":
        if temp[0] != "." and temp[-1] != ".":
            break
        elif temp[0] == ".":
            temp = temp[1:]
        elif temp[-1] == ".":
            temp = temp[:-1]
    if temp == "":
        temp +="a"
    if len(temp) >= 16:
        temp = temp[:15]
        while temp != "":
            if temp[-1] != ".":
                break
            elif temp[-1] == ".":
                temp = temp[:-1]
    if len(temp) <= 2:
        while len(temp) < 3:
            temp += temp[-1]
    answer = temp
    return answer