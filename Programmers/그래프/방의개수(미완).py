next_num = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
#next_num = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

from collections import defaultdict
from collections import Counter
def solution(arrows):
    graph = defaultdict(lambda :[])
    before, after = [0,0], [0,0]
    
    for arrow in arrows:
        after[0] = before[0] + next_num[arrow][0]
        after[1] = before[1] + next_num[arrow][1]
        graph[tuple(before)].append(tuple(after))
        graph[tuple(after)].append(tuple(before))
        before = after[:]
    for i in graph:
        graph[i] = list(set(graph[i]))

    stack = [(0,0)]
    visited = []
    while stack :
        current = stack.pop()
        visited.append(current)
        for next_node in graph[current]:
            if next_node not in visited:
                stack.append(next_node)
    
    hi= Counter(visited).values()
    
    answer = 0
    for h in hi :
        if h != 1 : answer+=(h-1)
    return answer
