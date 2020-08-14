# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
from collections import deque
from copy import deepcopy


ROAD, WALL = 0, 1      
NORMAL, CRASHED = 0, 1
IMPOSSIBLE = -1

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(R, C, board, distance, queue):
    while queue:
        row, col, mode = queue.popleft()

        # 도착점 => 이동한 거리 return
        if (row, col) == (R - 1, C - 1):
            return distance[mode][row][col]

        # 주변 탐색
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if n_row < 0 or n_row >= R or n_col < 0 or n_col >= C:
                continue
            if distance[mode][n_row][n_col]: # 해당 모드에서 이미 다녀온 경로
                continue
            
            # 벽이 아닌 경우 => 거리 갱신
            if board[n_row][n_col] == ROAD:
                distance[mode][n_row][n_col] = distance[mode][row][col] + 1 # 모드 유지 및 거리 갱신
                queue.append((n_row, n_col, mode))

            # 벽이 있을 경우 + 벽을 아직 부시지 않은 상태 => 벽뿌 가능
            if board[n_row][n_col] == WALL and mode == NORMAL:
                distance[CRASHED][n_row][n_col] = distance[mode][row][col] + 1 # 모드 변경 CRASHED => 벽을 부신 상태
                queue.append((n_row, n_col, CRASHED))

    return IMPOSSIBLE


def solution(R, C, board):
    answer = 0
    distance = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(2)]  # 해당 지점까지 이동한 거리를 담을 배열 => 2*R*C 

    queue = deque()
    queue.append((0, 0, NORMAL))
    distance[NORMAL][0][0] = 1 # 벽을 안부신 상태, 시작점 => 거리 1로 세팅

    answer = bfs(R, C, board, distance, queue)

    return answer


R, C = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(R)]
print(solution(R, C, board))


"""
5 5
00001
11011
00000
11111
11110

distance[0] - 벽을 부시지 않고 이동한 거리
[1, 2, 3, 4, 0]
[0, 0, 4, 0, 0]
[7, 6, 5, 6, 7]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]

distance[1] - 벽을 부신 상태에서 이동한 거리
[3, 4, 5, 6, 5]
[8, 7, 4, 7, 8]
[3, 4, 5, 6, 7]
[8, 7, 6, 7, 8]
[0, 0, 0, 0, 9]

"""