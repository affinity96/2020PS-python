T= int(input())

#for t in range(T): test_case.append(int(input()))
test_cases = [int(input()) for _ in range(T)]

for N in test_cases:
    P = [0,1,1,1,2,2]
    if (N<6) : print(P[N])
    else:
        for n in range(6,N+1):
            P.append(P[n-1]+P[n-5])
        print(P[N])
