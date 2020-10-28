# 로봇 청소기
# https://www.acmicpc.net/problem/14503

EMPTY, WALL, CHECK = 0, 1, 2
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3:(0, -1)}

# 주의 4방향 탐색
def is_completed(board, row, col):
    for dr, dc in directions.values():
        n_row, n_col = row + dr, col + dc

        if board[n_row][n_col] == EMPTY:
            return False
    
    return True

def solution(R, C, board, start):
    answer = 0
    row, col, cur_dir = start

    # 청소 시뮬레이션
    while True:
        # 1. 청소하기
        board[row][col] = CHECK
        answer += 1

        # 2. 탐색하기
        while True:
            left = (cur_dir + 3) % 4
            l_row, l_col = row + directions[left][0], col + directions[left][1]

            # a.
            if board[l_row][l_col] == EMPTY:
                cur_dir = left
                row, col = l_row, l_col
                break

            # c & d
            if is_completed(board, row, col):
                back = (cur_dir + 2) % 4
                b_row, b_col = row + directions[back][0], col + directions[back][1]

                # d
                if board[b_row][b_col] == WALL:
                    return answer
                
                row, col = b_row, b_col
                continue
        
            # b.
            cur_dir = left

R, C = map(int, input().split())
start = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
print(solution(R, C, board, start))