def solution(n, results):
    answer = 0
    boxing_result = [[4500 for _ in range(n+1)]for _ in range(n+1)]
    for [a,b] in results: boxing_result[a][b] = 1
    #플로이드 워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if boxing_result[i][j] > boxing_result[i][k] + boxing_result[k][j]:
                    boxing_result[i][j] = boxing_result[i][k] + boxing_result[k][j]           
    for i in range(1, n+1):
        count = n 
        for j in range(1, n+1):
            if boxing_result[i][j] != 4500 : count -=1
            if boxing_result[j][i] !=4500 : count-=1
        if count == 1 : answer+=1

    
    return answer
