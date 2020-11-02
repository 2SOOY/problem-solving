# 감시
# https://www.acmicpc.net/problem/15683
from copy import deepcopy

EMPTY, WALL, CHECK = 0, 6, -1

# 방향 및 cctv 감시 영역 표현하기
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
U, R, D, L = 0, 1, 2, 3

cctv_info = {1: [(R,), (D,), (L,), (U,)], 
        2: [(R, L), (U, D)],
        3: [(U, R), (R, D), (D, L), (L, U)],
        4: [(L, U, R), (U, R, D), (R, D, L), (D, L, U)],
        5: [(L, U, R, D)]}

answer = float('inf') # 사각지대 개수

# 주어진 board에서 cctv들의 정보를 가져오는 함수
def get_cctv(R, C, board):
    result = []

    for row in range(R):
        for col in range(C):
            if 1 <= board[row][col] <= 5:
                result.append((board[row][col], row, col))

    return result

# cctv 감시 결과 사각지대 개수 구하는 함수
def calculate(R, C, board):
    answer = 0

    for row in range(R):
        for col in range(C):
            if board[row][col] == EMPTY:
                answer += 1
    return answer


# cctv를 통한 감시하기 (4방향에 대해)
def dfs(R, C, board, cctvs, level):
    global answer

    # 모든 cctv 방향 결정 완료
    if level == len(cctvs):
        answer = min(answer, calculate(R, C, board))
        return
    
    # 현재 cctv의 방향 결정 및 감시하기
    cur, row, col = cctvs[level]
    for dirs in cctv_info[cur]:
        temp = deepcopy(board) # 감시 상태 복사본을 기준으로 각방향(90, 180, 270, 360) 탐색

        for direction in dirs:
            n_row, n_col = row, col

            # 주어진 방향(U, R, L, D)에 대해 감시하기
            while True:
                n_row, n_col = n_row + delta[direction][0], n_col + delta[direction][1]
                if n_row < 0 or n_row >= R or n_col < 0 or n_col >= C \
                or temp[n_row][n_col] == WALL: # 감시 종료
                    break

                if temp[n_row][n_col] != EMPTY:
                    continue

                temp[n_row][n_col] = CHECK

        dfs(R, C, temp, cctvs, level + 1) # 다음 CCTV에 대해 탐색


def solution(R, C, board):
    global answer
    cctvs = get_cctv(R, C, board)
    dfs(R, C, board, cctvs, 0)

    return answer

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
print(solution(R, C, board))