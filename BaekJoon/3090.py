N, T = map(int, input().split(' '))
def canI(cha,num_arr):
    change = 0
    semi_num = num_arr[:]
    
    for i in range(N-1):
        if semi_num[i+1] - semi_num[i] > cha : 

            change += semi_num[i+1] - semi_num[i] - cha
            semi_num[i+1] = semi_num[i] + cha

    for j in range(N-1, 0, -1):
        if semi_num[j-1] - semi_num[j] > cha : 
            change += semi_num[j-1] - semi_num[j] - cha
            semi_num[j-1] = semi_num[j] + cha
    if change <= T :
        return semi_num
    else : 
        return False
def main():
    
    num_arr = [int(i) for i in input().split(' ')]
    left = 0
    right = 10000001

    while left<=right:
        mid = (left+right)//2
        hello = canI(mid,num_arr)
        if hello:
            result = hello[:]
            right = mid-1
        else:
            left = mid+1

    a = [str(i) for i in result]
    print(' '.join(a))

if __name__ == '__main__': main()
