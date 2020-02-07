def solution(arrangement):
    gwal_stack = []
    answer = 0
    #레이저 구분해놓기
    arrangement = arrangement.replace('()','l')
    for (i, gwal) in enumerate(arrangement):
        #열린괄호 -> 스택추가
        if gwal == '(' : 
            gwal_stack.append('(')
        #닫힌괄호 -> 스택 팝 후 절단 1개
        elif gwal == ')':
            gwal_stack.pop()
            answer+=1
        #레이저 만나면 -> 지금까지 생 열린괄호 (닫힌괄호 만나지 않은 열린괄호) 갯수만큼 절단    
        elif gwal == 'l':
            answer += len(gwal_stack)
    
    
    return answer
