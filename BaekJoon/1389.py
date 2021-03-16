N,M = map(int, input().split(' '))

connection = []
result_list = []

#최솟값들의 집합
distance = [[50000 for _ in range(N)] for _ in range(N)]

#친구관계 설정하기 연결된 친구끼리의 distance는 1
for m in range(M):
    First, Second = map(int, input().split(' '))
    connection.append([First, Second])
    distance[First-1][Second-1] = 1
    distance[Second-1][First-1] = 1

#플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

#친구관계의 distance를 자신을 제외하고 더함
for person, connect_statement in enumerate(distance):
    result = 0
    for i, friend in enumerate(connect_statement):
        if person == i : continue
        else : result += friend
    result_list.append(result)
print(result_list.index(min(result_list))+1)
