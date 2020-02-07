def solution(progresses, speeds):
    answer = []
    while(progresses):
        for i, (progress, speed) in enumerate(zip(progresses, speeds)):
            progress = progress + speed
            progresses[i] = progress     
        count=0
        for p in range(len(progresses)):
            print(progresses)
            if progresses[0] >= 100 :
                progresses.pop(0)
                speeds.pop(0)
                count+=1
            else : break
        if count!=0 : answer.append(count)
    
    return answer
