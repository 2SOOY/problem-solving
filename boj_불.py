# 불
# https://www.acmicpc.net/problem/5427

from collections import deque

EMPTY, WALL, START, FIRE = '.', '#', '@', '*'
IMPOSSIBLE = "IMPOSSIBLE"
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 불 퍼뜨리기
def bfs_fire(R, C, board, fires):
    # 현재 존재하는 불의 영역만큼(len(fires))만 bfs
    for _ in range(len(fires)): 
        row, col = fires.popleft()
        
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if 0 <= n_row < R and 0 <= n_col < C \
            and board[n_row][n_col] == EMPTY:

                board[n_row][n_col] = FIRE
                fires.append((n_row, n_col))
    return


# 탈출 가능 여부 파악 함수
def is_exit(R, C, row, col):
    # 테두리에 위치한다면 탈출 가능
    if row == 0 or row == R - 1 or col == 0 or col == C - 1:
        return True
    
    return False


# 사람 이동하기
def bfs_move(R, C, board, checked, queue):
    # 현재 위치 이동이 가능한 만큼만 bfs - 불 퍼짐과 같은 맥락
    for _ in range(len(queue)):
        row, col, step = queue.popleft()
        
        if is_exit(R, C, row, col):
            return step

        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if 0 <= n_row < R and 0 <= n_col < C \
            and board[n_row][n_col] == EMPTY \
            and checked[n_row][n_col] == False:

                queue.append((n_row, n_col, step + 1)) 
                checked[n_row][n_col] = True

    return -1

def solution(R, C, board):
    fires = deque() # 불이 퍼진 영역
    queue = deque() # 사람이 이동한 영역
    checked = [[False] * C for _ in range(R)] # 사람 이동시 체크 배열

    for row in range(R):
        for col in range(C):
            if board[row][col] == START:
                queue.append((row, col, 1))
                checked[row][col] = True

            if board[row][col] == FIRE:
                fires.append((row, col))
    
    while True:
        answer = 0

        # 불 퍼뜨리기
        bfs_fire(R, C, board, fires)

        # 이동하기
        answer = bfs_move(R, C, board, checked, queue)
        
        if answer != -1:
            return answer
        
        # 더 이상 탐색이 불가능하다 => IMPOSSIBLE
        if len(fires) == 0 and len(queue) == 0:
            break

    return IMPOSSIBLE

T = int(input())
for _ in range(T):
    C, R = map(int, input().split())
    board = [list(input()) for _ in range(R)]

    print(solution(R, C, board))
    