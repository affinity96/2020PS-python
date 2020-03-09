from collections import defaultdict
def solution(n, edge):
    node_dic = defaultdict(lambda :[])
    distance_from1_dic = [-1 for k in range(n+1)]
    distance_from1_dic[1] = 0
    bfs_queue = [1]
    for each_edge in edge:
        node_dic[each_edge[0]].append(each_edge[1])
        node_dic[each_edge[1]].append(each_edge[0])
    max_num = 0
    while bfs_queue:
        a = bfs_queue.pop()

        for i in node_dic[a]:
            #이게 진짜 레알 개쩜 visited를 안쓰고 거리가 -1이면 방문을 안한거니까 이케하니까 통과됐네 와씨 진짜 야마가 알딸딸
            if distance_from1_dic[i] == -1 :
                bfs_queue.insert(0,i)
                dis = (distance_from1_dic[a]+1)
                distance_from1_dic[i] = dis
                if dis > max_num : max_num = dis
    answer = 0
    print(distance_from1_dic)

    answer = distance_from1_dic.count(max_num)
    
    return answer
