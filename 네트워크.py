def DFS(V,E):
    Color = []
    #필요는 없지만 time을 저장하는 d와 f리스트
    d = [0 for _ in range(len(V))]
    f = [0 for _ in range(len(V))]
    #찾고자하는 뭉탱이
    moong = 0
    ADJ = [[]for _ in range(len(V))]
    for (a,b) in E:
        ADJ[a].append(b)

    #초기화
    for v in range(len(V)) :
        Color.append('white')
    
    for u in range(len(V)):
        if Color[u]=='white':
            DFS_Visit(V,u,Color,d,f,ADJ)
            #이거 한 루프당 한 뭉탱이가 블랙이 되었을 것이므로 뭉탱이+1
            moong += 1
            
    return moong

def DFS_Visit(V,u,Color,d,f,ADJ):
    time = 0
    #방문 노드 색깔 그레이로 바꿈
    Color[u] = 'gray'
    time +=1
    d[u] = time
    
    for v in ADJ[u]:
        print(v)
        #연결된 주변노드 색 화이트라면
        if Color[v] == 'white': 
            #재귀!
            DFS_Visit(V,v,Color,d,f,ADJ)
    #다돌았으면(주변 연결노드중 화이트가없으면) 블랙으로 바꿔
    Color[u] = 'black'

    time +=1
    f[u] = time
    
def solution(n, computers):
    
    V, E = [], []
    for num in range(n) :
        V.append(num)
    for com,net in enumerate(computers):
        for connect_num, connect in enumerate(net):
            if connect == 1:
                if com != connect_num:
                    E.append((com,connect_num))
    answer = DFS(V,E)
    return answer
    
