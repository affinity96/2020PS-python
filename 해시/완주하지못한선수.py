def solution(participant, completion):
    answer = {p : 0 for p in set(participant)}
    for par in participant: answer[par] +=1
    for com in completion : answer[com] -=1
    for result in answer : 
        if answer[result] == 1 :return result
