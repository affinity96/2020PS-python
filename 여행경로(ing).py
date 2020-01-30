def makeEdge(tickets_new):
    edge = dict()
    start_nodes = []
    #일단 엣지 딕셔너리 설정. 이때 각 티켓이 노드이므로 티켓을 키값으로 초기화
    for ticket in tickets_new:
        edge.setdefault(ticket,[])
        #초기화 하는 김에 ICN으로부터 출발하는 노드들을 startnode라고 함. 
        if(ticket[0]=="ICN"):
            start_nodes.append(ticket)
    #각 키의 연결 노드는 해당 키의 도착지가 출발지가 되는 노드들.
    for (first_departure, first_arrival) in tickets_new:
        for (next_departure,next_arrival) in tickets_new:
            if first_arrival == next_departure:
                edge[(first_departure, first_arrival)].append((next_departure,next_arrival))
    return edge, start_nodes

def DFS(tickets, edge, node,visited,answer):
    
    visited.append(node)
    answer.append(node[1])
    for next_node in edge[node]:
        if next_node not in visited:
            DFS(tickets, edge, next_node,visited,answer)
    return answer
    
        
        
def solution(tickets):
    # 리스트는 딕셔너리의 키값으로 될 수 없어서 튜플로 바꿔줌 
    tickets_new = []
    for ticket in tickets:
        ticket = tuple(ticket)
        tickets_new.append(ticket)
    tickets_new = sorted(tickets_new)
    edge, start_nodes = makeEdge(tickets_new)
    
    for start_node in start_nodes:
        answer = ["ICN"]
        visited = []
        answer = DFS(tickets_new, edge, start_node, visited, answer)
        print(answer)
        if len(visited)==len(tickets_new) : return answer
        else : continue
