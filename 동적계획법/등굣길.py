def solution(m, n, puddles):
    #초기화
    load_count = [[1 for _ in range(m)]for _ in range(n)]
    #집은 0으로
    load_count[0][0] = 0
    for puddle in puddles : 
        #첫째줄에 웅덩이가 있다면 -> 그 웅덩이 이후의 첫번째 세로열은 0으로. 웅덩이 이후로는 접근할 수 없으므로
        if puddle[0] == 1 : 
            for i in range(puddle[1]-1,n): 
                load_count[i][0] = 0
        #마찬가지로 가로열
        elif puddle[1] == 1 : 
            for i in range(puddle[0]-1,m): 
                load_count[0][i] = 0
        #가로세로 첫 라인을 제외한 웅덩이 0으로        
        else :load_count[puddle[1]-1][puddle[0]-1] = 0
            
    for x in range (1, n):
        for y in range(1, m):
            #그 칸의 경로는 바로위, 바로 왼쪽의 합과같음
            if load_count[x][y] !=0 : load_count[x][y] = (load_count[x][y-1] + load_count[x-1][y])%1000000007
    print(load_count)
    answer = load_count[n-1][m-1]
    return answer
