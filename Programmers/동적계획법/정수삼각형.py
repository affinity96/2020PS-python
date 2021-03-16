def solution(triangle):
    for level, level_list in enumerate(triangle) :
        if level==0 : continue
        for i, number in enumerate (level_list):
            if i == 0: level_list[i] = number+triangle[level-1][0]
            elif i == len(level_list)-1 : level_list[i] = number+triangle[level-1][-1]
            else:
                level_list[i] = max(number+triangle[level-1][i-1], number+triangle[level-1][i])
            
    answer = max(triangle[-1])
    return answer
