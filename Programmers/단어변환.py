from collections import deque
def makeEdge(words):
    edge = dict()
    for word in words:
        edge.setdefault(word,[])
    
    for word1 in words:
        for word2 in words:
            count = 0
            for i in range(len(word1)):
                if word1[i]==word2[i] : count +=1
            if count == len(word1)-1:
                edge[word1].append(word2)
    return edge

def solution(begin, target, words):
    if target not in words : return 0
    else:
        words.append(begin)
        edge = makeEdge(words)
        #print("edge",edge)
        
        bfs_queue = deque()
        bfs_queue.append(begin)
        distance = dict()
        #모든 distance를 0으로 초기화 
        for word in words:
            distance.setdefault(word,0)
            
        visited = []
        
        while bfs_queue:
            visit_word = bfs_queue.popleft()
            visited.append(visit_word)
            for new_word in edge[visit_word]:
                
                if new_word not in visited:
                    print(new_word)
                    if new_word not in bfs_queue:
                        bfs_queue.append(new_word)
                        distance[new_word] = distance[visit_word]+1
        answer = distance[target]            
        return answer
