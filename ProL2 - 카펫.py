def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(yellow, 0, -1):
        if yellow % i == 0 and (i + 2) * ((yellow // i) + 2 ) == total:
            answer.append(i + 2)
            answer.append((yellow // i) + 2 )
            break
    return answer