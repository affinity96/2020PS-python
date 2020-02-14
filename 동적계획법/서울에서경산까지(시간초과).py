def solution(K, travel):
    total_map = []
    for city_index ,city in enumerate(travel):
        total_map.append([[0,0]for _ in range(2 ** (city_index+1))])
    total_map[0][0] = [travel[0][0],travel[0][1]]
    total_map[0][1] = [travel[0][2],travel[0][3]]
    
    for next_city in range(1, len(travel)):
        
        for i, city in enumerate(total_map[next_city]):
            index = int(i/2)
            if total_map[next_city-1][index][0] == -1: continue
            else:
                #도보
                if i % 2 == 0 :
                    time=total_map[next_city-1][index][0]+ travel[next_city][0]
                    if time <= K : 
                        city[0] = time
                        city[1] = total_map[next_city-1][index][1]+ travel[next_city][1]
                    else : city[0] = -1
                #바이크        
                else :
                    time=total_map[next_city-1][index][0]+ travel[next_city][2]
                    if time <= K : 
                        city[0] = time
                        city[1] = total_map[next_city-1][index][1]+ travel[next_city][3]
                    else : city[0] = -1
    money_list = []

    for m in total_map[-1]: money_list.append(m[1])
    return max(money_list)
