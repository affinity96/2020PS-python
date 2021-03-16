N = int(input())

distance = [0 for _ in range(N+1)]

for x, current in enumerate(distance):
    if x<2 : continue
    distance[x] = distance[x-1]+1
    if (x % 3) == 0 : distance[x] = min(distance[int(x/3)]+1, distance[x])
    if (x%2) == 0 : distance[x] = min(distance[int(x/2)]+1, distance[x])

print(distance[N])

