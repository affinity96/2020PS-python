T= int(input())
#for t in range(T): test_case.append(int(input()))
test_cases = [int(input()) for _ in range(T)]
padoban = [0,1,1,1,2,2]

def P(n) : 
    if n<6 : return padoban[n]
    else : 
        return P(n-1)+P(n-5)

for N in test_cases:
    print(P(N))
