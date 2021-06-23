import heapq
def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(n):
        m = heapq.heappop(works)
        m += 1
        heapq.heappush(works, m)
    answer = 0
    for i in range(len(works)):
        tmp = heapq.heappop(works)
        if tmp > 0:
            tmp = 0
        answer += (tmp ** 2)
    return answer
