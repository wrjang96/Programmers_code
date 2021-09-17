def solution(numbers):
    answer_arr = [0,1,2,3,4,5,6,7,8,9]
    answer = sum(list(set(answer_arr).difference(numbers)))
    return answer