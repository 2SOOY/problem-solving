# 음식물 피하기
# https://www.acmicpc.net/problem/1743

import sys
sys.setrecursionlimit(10 ** 6)

EMPTY, FULL = 0, 1
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(R, C, board, check, row, col):
    check[row][col] = True
    result = 1

    for dr, dc in delta:
        n_row, n_col = row + dr, col + dc

        if 0 <= n_row < R and 0 <= n_col < C \
        and board[n_row][n_col] == FULL \
        and check[n_row][n_col] == False:

            result += dfs(R, C, board, check, n_row, n_col)

    return result


def solution(R, C, board):
    check = [[False] * C for _ in range(R)]
    answer = 0

    for row in range(R):
        for col in range(C):
            if board[row][col] == EMPTY or check[row][col]:
                continue

            answer = max(answer, dfs(R, C, board, check, row, col))

    return answer


R, C, K = map(int, input().split())
board = [[0] * C for _ in range(R)]

for _ in range(K):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c] = FULL

print(solution(R, C, board))
