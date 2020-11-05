# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913
from copy import deepcopy

def solution(land):
    answer = 0
    R = len(land)
    
    for row in range(1, R):
        for col in range(4):
            cur = land[row][col]

            for i in range(4):
                if col == i:
                    continue

                land[row][col] = max(land[row][col], cur + land[row - 1][i])

    answer = max(land[-1])
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))