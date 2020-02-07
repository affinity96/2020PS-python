def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    answer = 0
    
    bridge[0] = truck_weights.pop(0)
    answer+=1
    
    while(sum(bridge)>0):
        
        answer +=1
        bridge.insert(0,0)
        bridge.pop()
        if(truck_weights):
            if(sum(bridge)+truck_weights[0] <= weight):
                bridge[0] = truck_weights.pop(0)
                
        
    return answer
