def solution(n, times):
    times = sorted(times)
    answer = 0
    min_time = 0
    max_time = n * times[-1]
    mid_time = (max_time + min_time) //2

    while max_time > min_time :
        person_sum = 0
        for time in times: person_sum += mid_time//time
        print(mid_time, person_sum)
        
        if person_sum < n:
            min_time = mid_time+1
            mid_time = (max_time + min_time) // 2
        else:
            max_time = mid_time
            mid_time = (max_time+min_time) //2 
        
    return mid_time
