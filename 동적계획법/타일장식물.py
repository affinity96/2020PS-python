Dool = [-1,4,6]
for _ in range(77) : Dool.append(-1)
def solution(N):
    if Dool[N] != -1 : return Dool[N]
    else:
        Dool[N] = solution(N-1)+solution(N-2)
        return Dool[N]
