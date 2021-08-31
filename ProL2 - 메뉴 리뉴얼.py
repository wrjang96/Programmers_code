import itertools

def solution(orders, course):
    alphabet = set()
    idx = 0
    ordered_menus = [[] for i in range(len(orders))]
    for ordered_set in orders:
        for alphabets in ordered_set:
            alphabet.add(alphabets)
            ordered_menus[idx].append(alphabets)
        idx += 1
    alphabet = list(alphabet)
    alphabet.sort()
    answer = []
    for num in course:
        temp_answer = []
        temp = set([])
        for order in orders:
            tmp = itertools.combinations(order, num)
            tmp = list(set(tmp))
            for i in range(len(tmp)):
                temp.add(tmp[i])

        temp = list(set(temp))
        temp.sort()
        maxcnt =0
        for possible_menu in temp:
            possible_menu = list(possible_menu)
            possible_menu.sort()
            cnt = 0
            for ordered_menu in ordered_menus:
                temp_common = list(set(possible_menu) & set(ordered_menu))
                temp_common.sort()
                if temp_common == possible_menu:
                    cnt += 1
            if cnt > maxcnt and cnt >= 2:
                maxcnt = cnt
                temp_answer.clear()
                temp_answer.append(possible_menu)
            elif cnt == maxcnt and cnt >= 2:
                maxcnt = cnt
                temp_answer.append(possible_menu)
        tmp_str_answer = []
        for i in range(len(temp_answer)):
            tmp_str = ""
            for j in temp_answer[i]:
                tmp_str +=j
            tmp_str_answer .append(tmp_str)
        answer += tmp_str_answer
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))