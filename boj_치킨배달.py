# 치킨 배달
# https://www.acmicpc.net/problem/15686
from itertools import combinations
from copy import deepcopy

EMPTY, HOME, CHICKEN = 0, 1, 2
MAX = float('inf')

# 집, 치킨집 좌표 얻어오는 역할
def get_spots(N, board):
    homes = []
    chickens = []

    for row in range(N):
        for col in range(N):
            if board[row][col] == HOME:
                homes.append((row, col))
                continue

            if board[row][col] == CHICKEN:
                chickens.append((row, col))
    
    return [homes, chickens]

# M개의 치킨집을 선택하는 함수
def get_candidates(chickens, M):
    candidates = combinations(chickens, M)
    return candidates

# 집 ~ 치킨집 사이의 거리
def calc_cost(src, dst):
    s_row, s_col = src
    d_row, d_col = dst

    return abs(s_row - d_row) + abs(s_col - d_col)


def solution(N, M, board):
    answer = MAX

    homes, chickens = get_spots(N, board)
    candidates = get_candidates(chickens, M)

    for candidate in candidates:
        temp_total_cost = 0
        for home in homes:
            min_cost = min([calc_cost(home, chicken) for chicken in candidate]) # 집 ~ 치킨집 최소 거리
            temp_total_cost += min_cost # 도시의 치킨 거리
        
        answer = min(answer, temp_total_cost)
        
    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))

