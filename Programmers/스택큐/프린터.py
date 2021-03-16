def solution(priorities, location):
    answer = 0
    while(priorities):
        flag = 0
        for i in range(1,len(priorities)):
            if priorities[0] < priorities[i]:
                priorities.append(priorities.pop(0))
                if location > 0 : location-=1
                else : location = len(priorities)-1
                flag = 1
                break
        if flag == 0 : 
            priorities.pop(0)
            answer += 1
            if location == 0 : return answer
            else : location -=1
