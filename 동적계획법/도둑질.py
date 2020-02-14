def solution(money):
    #case1 : 첫집 털고 마지막집 안털고, case2 : 첫집 안털고 마지막집 털고
    case1 = [0 for _, _ in enumerate(money)]
    case2 = [0 for _, _ in enumerate(money)]
    #첫집 털면 그 다음집은 뭐가 됐든 털수 없는데 참조해야하니까 첫집 수로 ㄱㄱ
    case1[0] = money[0]
    case1[1] = money[0]
    #전후로 어딜터는게 이득일까 탐색하면서 갱신. 마지막집 털면안되니까 len-1
    for thief in range(2, len(money)-1):
        case1[thief] = max(case1[thief-1], money[thief]+case1[thief-2])
    #첫집 안터는거면 두번째집 턴다는거. 첫집은 없는셈 쳐야하니 0
    case2[0] = 0
    case2[1] = money[1]
    
    for thief2 in range(2, len(money)):
        case2[thief2] = max(case2[thief2-1],  money[thief2]+case2[thief2-2])
    
    return max(case1[-2],case2[-1])
    return answer
