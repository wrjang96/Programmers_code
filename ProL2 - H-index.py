def solution(citations):
    citations.sort()
    answer = 0
    for i in range(citations[-1], 0, -1):
        print(i)
        upcnt =0
        downcnt =0
        for j in range(len(citations)):
            if i <= citations[j]:
                upcnt += 1
            if i >= citations[j]:
                downcnt += 1
        print(upcnt, downcnt)
        if upcnt >= i and downcnt <= i:
            answer = i
            #print(answer)
            break
    return answer