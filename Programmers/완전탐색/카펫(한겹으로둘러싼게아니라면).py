def redDecomposition(red):
    red_list=[]
    if red == 1 : return [(1,1)]
    for r_sero in range(1, int(red/2)+1):
        r_garo = red/r_sero
        r_trash = red%r_sero
        if r_sero > r_garo : break
        if r_trash == 0:
            red_list.append((r_sero,int(r_garo)))
    return red_list

def calculateBrown(m,n,r_sero,r_garo):
    brown_temp = 2*n*r_garo + 2*m*r_sero + 4*m*n
    return brown_temp

def solution(brown, red):
    
    red_list = redDecomposition(red)
    for (r_sero, r_garo) in red_list:
        for m in range(1,2500):
            for n in range(1,2500):
                brown_temp = calculateBrown(m,n,r_sero,r_garo)
                if brown == brown_temp : 
                    return[r_garo+2*m, r_sero+2*n]
        
