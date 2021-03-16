T= int(input())
#for t in range(T): test_case.append(int(input()))
test_cases = [int(input()) for _ in range(T)]

padoban = [0,1,1,1,2,2]
for i in range(95): padoban.append(-1) 

def P(n) : 
    if padoban[n] != -1 : return padoban[n]
    else:
        padoban[n] = P(n-1) + P(n-5)
        return padoban[n]

for N in test_cases:
    print(P(N))
