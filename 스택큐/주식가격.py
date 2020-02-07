def solution(prices):
    answer = []
    length = len(prices)
    for (i,price) in enumerate(prices):
        flag = 0
        for j in range(i+1,length):
            if price > prices[j]: 
                answer.append(j-i)
                flag = 1
                break
    #끝까지 간 놈들은 결국 전체길이 - (인덱스+1)만큼의 값을 가짐            
        if flag == 0:
            answer.append(length-i-1)
        
    return answer
