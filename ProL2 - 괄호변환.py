def check_right_str(arr):
    stack = 0
    return_value = True
    for i in range(len(arr)):
        if arr[i] == ")":
            stack += -1
        elif arr[i] == "(":
            stack += 1
        if stack < 0:
            return_value = False
    return return_value


def return_u_v(p):
    return_value = []
    stack = 0
    for i in range(len(p)):
        if p[i] == ")":
            stack -= 1
        elif p[i] == "(":
            stack += 1
        if stack == 0:
            return_value.append(p[:i + 1])
            return_value.append(p[i + 1:])
            break
    return return_value

def reverse(strings):
    r = {"(" : ")", ")": "("}
    return [r[s] for s in strings]

def recursive_answer(p):
    answer = ""
    if p != '':
        temp_temp = return_u_v(p)
        u = temp_temp[0]
        v = temp_temp[1]
        ## 3
        if check_right_str(u)== True:
            temp_ans = recursive_answer(v)
            answer = u + temp_ans
            return answer
        else:
            temp_str = u[1:-1]
            temp_str_arr = reverse(temp_str)
            temp_str = ""
            for data in temp_str_arr:
                temp_str += data
            answer = "(" + recursive_answer(v) + ")" + temp_str
            return answer
    else:
        return answer


def solution(p):
    answer = recursive_answer(p)
    return answer

solution("()))((()")
# def check_right_str(arr):
#     stack = 0
#     return_value = True
#     for i in range(len(arr)):
#         if arr[i] == ")":
#             stack += -1
#         elif arr[i] == "(":
#             stack += 1
#         if stack < 0:
#             return_value = False
#     return return_value
#
#
# def return_u(p):
#     return_value = []
#     stack = 0
#     for i in range(len(p)):
#         if p[i] == ")":
#             stack -= 1
#         elif p[i] == "(":
#             stack += 1
#         if stack == 0:
#             return_value.append(p[:i + 1])
#             return_value.append(p[i + 1:])
#             break
#     return return_value
#
#
# def recursive_answer(p):
#     answer = ""
#     if p != '':
#         first_flag = check_right_str(p)
#         if first_flag == True:
#             answer = p
#             return answer
#         else:
#             temp = p
#             print(temp)
#             while temp:
#                 temp_arr = return_u(temp)
#                 u = temp_arr[0]
#                 v = temp_arr[1]
#                 if check_right_str(u) == True:
#                     temp_ans = recursive_answer(v)
#                     answer = u + temp_ans
#                     return answer
#                 else:
#                     temp_str = u[1:-1]
#                     temp_str = temp_str[::-1]
#                     answer = "(" + recursive_answer(v) + ")" + temp_str
#                     return answer
#                 temp = v
#     return answer
#
#
# def solution(p):
#     answer = recursive_answer(p)
#     return answer