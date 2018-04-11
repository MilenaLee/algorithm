def solution(N):
    # write your code in Python 3.6
    
    max = 0
    local_max = 0
    flag = False
    
    while N:
        if N%2:
            if flag:
                max = max if max > local_max else local_max
            local_max = 0
            flag = True
        else:
            local_max += 1
        
        N = N // 2
            
    return max