import itertools
def isItSosu(number):
    
    if number < 2 : return False
    if number == 2 : return True
    if number % 2 == 0 : return False
    for i in range(3, number, 2) : 
        if number % i == 0 : return False
    return True

def solution(numbers):
    answer = 0
    for length,_ in enumerate(numbers):
        numbers_list = list(set(map(''.join, itertools.permutations(numbers,length+1))))
        
        for number in numbers_list:
            
            if number[0]!='0' : 
                if isItSosu(int(number)):

                    answer+=1

    return answer
