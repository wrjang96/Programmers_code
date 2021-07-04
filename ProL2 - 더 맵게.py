import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    while heap[0] < K:
        if len(heap) < 2:
            answer = - 1
            break
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        answer +=1
    return answer