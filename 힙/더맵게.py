import heapq
#그냥 scoville로 하니까 왜 안되지.. heap = []을 만들고 하니까 됨
def solution(scoville, K):
    length = len(scoville)
    heap=[]
    for num in scoville:
        heapq.heappush(heap, num)
    count = 0
    while length >0:
        a = heapq.heappop(heap)
        if length <= 1: 
            if a < K : return -1
            else : return count
        if a < K: 
            b = heapq.heappop(heap)
            c = a + (b*2)
            heapq.heappush(heap,c)
            length -=1
            count+=1
        else : return count    
