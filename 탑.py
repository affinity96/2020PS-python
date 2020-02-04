def solution(heights):
    answer = []
    plus = len(heights)
    for t in range(plus):
        transmit = heights.pop()
        a = -1
        if len(heights) == 0 : break
        while(heights):
            if heights[a] > transmit:
                answer.insert(0,a+plus)
                break
            if a <= (-1*(len(heights))) : 
                answer.insert(0,0)
                break
            else : a -=1
            print(a)
            
        plus -=1
            
    answer.insert(0,0)
    return answer
