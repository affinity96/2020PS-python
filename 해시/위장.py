from itertools import combinations
def solution(clothes):
    answer = 1
    clothes_count = {}

    for [cloth,jong] in clothes:
        if jong in clothes_count : clothes_count[jong] +=1
        else : 
            clothes_count[jong] = 1
    wear_count = list(clothes_count.values())
    for n in wear_count:
        answer *= n+1
    

    # for i in range(1, len(wear_count)+1):
    #     combi_list = list(combinations(wear_count,i))
    #     for combi in combi_list:
    #         temp = 1
    #         for n in combi: temp *= n
    #         answer+= temp
    return answer-1
