# 병든 나이트
# https://www.acmicpc.net/problem/1783

LIMIT = 4

def solution(R, C):
    if R == 1:
        return 1
    
    elif R == 2:
        if C <= 2:
            return 1
        
        elif 3 <= C < 5:
            return 2

        elif 5 <= C < 7:
            return 3
            
        else: 
            return LIMIT 

    # R >= 3
    else:
        if C == 1:
            return 1

        elif 2 <= C < 5:
            return C

        elif 5 <= C < 7:
            return LIMIT

        # C >= 7
        else:
            return C - 2


R, C = map(int, input().split())
print(solution(R, C))