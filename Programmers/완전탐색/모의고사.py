def solution(answers):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0
    
    for (i,j) in enumerate(answers) : 
        if j == supo_1[int(i%5)] :count1 +=1
        if j == supo_2[int(i%8)] : count2 +=1
        if j == supo_3[int(i%10)] :count3 +=1
    
    arr = {1 : count1, 2: count2, 3: count3}

    arr = sorted(arr.items(), key = lambda x : x[1], reverse= True)

    answer = []
    max_value = arr[0][1]
    for i, (k,v) in enumerate(arr):
        print(v)
        if v == max_value : 
            answer.append(k)
    answer = sorted(answer)
    return answer
