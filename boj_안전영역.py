# 안전 영역
# https://www.acmicpc.net/problem/2468
import sys
sys.setrecursionlimit(10 ** 6)


WATER = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def make_checked(N):
    return [[False] * N for _ in range(N)]


# 인접 영역 처리
def dfs(N, board, check, row, col):
    check[row][col] = True

    for dr, dc in delta:
        n_row, n_col = row + dr, col + dc

        if 0 <= n_row < N and 0 <= n_col < N \
        and board[n_row][n_col] != WATER \
        and check[n_row][n_col] == False:

            dfs(N, board, check, n_row, n_col)
   
    return


def solution(N, board):
    answer = 1 # 모든 건물의 높이가 같을 경우
    min_height = min([min(row) for row in board])
    max_height = max([max(row) for row in board])

    for height in range(min_height, max_height):
        temp_answer = 0

        # 건물 높이에 따른 물에 잠김
        for row in range(N):
            for col in range(N):
                if board[row][col] == WATER or board[row][col] > height:
                    continue
                board[row][col] = WATER
        
        # 안전 영역의 개수 세기
        check = make_checked(N)
        for row in range(N):
            for col in range(N):
                if board[row][col] != WATER and check[row][col] == False: # ** check 조건 주의
                    dfs(N, board, check, row, col)
                    temp_answer += 1
        
        answer = max(answer, temp_answer)
        
    return answer


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))