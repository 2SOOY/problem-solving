# 탈출
# https://www.acmicpc.net/problem/3055
from collections import deque

EMPTY, WATER, STONE = '.', '*', 'X'
SRC, DST = 'S', 'D'
IMPOSSIBLE = 'KAKTUS'

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 시작위치, 물위치 가져오는 함수
def get_info(R, C, board):
    waters = deque()
    src = []

    for row in range(R):
        for col in range(C):
            if board[row][col] == WATER:
                waters.append((row, col))
            
            if board[row][col] == SRC:
                src = deque([(row, col, 0)])

    return src, waters


# 물에 대해 bfs
def bfs_water(R, C, board, waters):
    for _ in range(len(waters)):
        row, col = waters.popleft()

        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if n_row < 0 or n_row >= R or n_col < 0 or n_col >= C:
                continue
            if board[n_row][n_col] == STONE or board[n_row][n_col] == DST or board[n_row][n_col] == WATER:
                continue

            board[n_row][n_col] = WATER
            waters.append((n_row, n_col))


# 고슴도치 bfs
def bfs(R, C, board, path):
    for _ in range(len(path)):
        row, col, step = path.popleft()
        
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if n_row < 0 or n_row >= R or n_col < 0 or n_col >= C:
                continue

            if board[n_row][n_col] == EMPTY:
                # 다음 위치 이동이 가능할 때, 해당 지역이 물에 인접한 지역인지 체크
                for ndr, ndc in delta:
                    nn_row, nn_col = n_row + ndr, n_col + ndc

                    if nn_row < 0 or nn_row >= R or nn_col < 0 or nn_col >= C \
                    or board[nn_row][nn_col] == WATER:
                        continue
                    
                    board[n_row][n_col] = SRC
                    path.append((n_row, n_col, step + 1))

            # 무사히 이동 가능
            if board[n_row][n_col] == DST:
                return step + 1

    return -1

def solution(R, C, board):
    path, waters = get_info(R, C, board)

    while path or waters:

        # 물 채우기 => 고슴도치 이동
        bfs_water(R, C, board, waters)
        result = bfs(R, C, board, path)

        if result != -1:
            return result

    # 이동 불가능
    return IMPOSSIBLE

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
print(solution(R, C, board))