# import itertools

# def solution(distance, rocks, n):
#     result = []
#     rocks = sorted(rocks)
#     remove_rocks = list(itertools.combinations(rocks,n))

#     for _ , remove_rock in enumerate(remove_rocks):
#         semi_rocks = rocks[:]
#         between_distance = []
        
#         for remove in remove_rock:
#             semi_rocks.remove(remove)

            
#         between_distance.append(semi_rocks[0])
#         for r in range(1, len(semi_rocks)):
#             between_distance.append(semi_rocks[r]-semi_rocks[r-1])
#         between_distance.append(distance-semi_rocks[-1])
#         result.append(min(between_distance))

#     answer = max(result)
#     return answer

import math
def howMuchRocksRemove(distance, rocks, n):

        prev = 0
        min_distance = math.inf
        remove_rock = 0
        for i, rock in enumerate(rocks):
            if rock - prev < distance: remove_rock +=1
            else :
                min_distance = min(min_distance, rock-prev)
                prev = rock
        if remove_rock > n : False
        else : return min_distance

def solution(distance, rocks, n):
    rocks = sorted(rocks)
    rocks.append(distance)
    left = 0
    right = distance
    answer = 0
    while left <= right:
        mid = (left+right)//2
        a=howMuchRocksRemove(mid, rocks, n)
        if a: 
            answer = a
            left = mid+1

        else : 
            right = mid-1
    return answer
