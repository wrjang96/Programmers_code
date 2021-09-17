def change_to_three(n):
    flag = False
    changed_str = ""
    for i in range(16,-1,-1):
        if n >= 3** i:
            cnt = 0
            while n >= 3** i:
                n -= 3**i
                cnt +=1
            flag = True
            changed_str += str(cnt)
        elif flag == True:
            changed_str +="0"
    return changed_str

def change_to_ten(n):
    answer = 0
    for i in range(len(n) - 1,-1,-1):
        answer += int(n[len(n) - i -1]) * 3**i
    return answer

def solution(n):
    temp_str = change_to_three(n)
    temp_str = temp_str[::-1]
    answer = int(change_to_ten(temp_str))
    return answer