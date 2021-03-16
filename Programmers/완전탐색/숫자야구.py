def baseballgame(number, question):
    strike, ball = 0,0
    number_s = str(number)
    question_s = str(question)
    if number_s[0]==question_s[0] : 
        strike+=1
    else:
        if number_s[0]==question_s[1] : ball+=1
        elif number_s[0]==question_s[2] : ball+=1   
    if number_s[1]==question_s[1] : 
        strike+=1
    else:
        if number_s[1]==question_s[2] : ball+=1
        elif number_s[1]==question_s[0] : ball+=1 
    if number_s[2]==question_s[2] : 
        strike+=1
    else:
        if number_s[2]==question_s[0] : ball+=1
        elif number_s[2]==question_s[1] : ball+=1  
    
    return (strike,ball)
        
def solution(baseball):
    answer = 0
    for number in range(123, 999):
    #중복제거
        if len(str(number)) > len(set(str(number))) : continue
    #0제거    
        elif str(number).count('0') : continue
        count = 0
        for question_arr in baseball:
            question = question_arr[0]
            if baseballgame(number,question) != (question_arr[1],question_arr[2]) : break
            else : count+=1
        if count == len(baseball) : answer +=1
    
    return answer
