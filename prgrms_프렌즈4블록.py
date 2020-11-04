# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679
from collections import deque

delta = [(0, 1), (1, 0), (1, 1)]
EMPTY = '0'

# 4개의 블록 터뜨릴 수 있는지 체크하는 함수
def is_possible(R, C, board, row, col):
    target = board[row][col]

    for dr, dc in delta:
        n_row, n_col = row + dr, col + dc
        if board[n_row][n_col] != target:
            return False
    
    return True


# 보드 업데이트 함수
def update_board(R, C, board, temp):
    result = 0

    # 4블록 없애기
    for row, col in temp:
        if board[row][col] != EMPTY:
            board[row][col] = EMPTY
            result += 1

        for dr, dc in delta:
            if board[row + dr][col + dc] != EMPTY:
                board[row + dr][col + dc] = EMPTY
                result += 1

    # 블록들 내리기 
    for col in range(C):
        temp_block = []
        temp_empty = []

        for row in range(R - 1, -1, -1):
            if board[row][col] == EMPTY:
                temp_empty.append(EMPTY)
            else:
                temp_block.append(board[row][col])
        
        temp_col = temp_empty + temp_block[::-1]

        for row in range(R):
            board[row][col] = temp_col[row]

    return result


def solution(R, C, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        temp = [] # 없앨 블록 좌표들을 담은 리스트

        # 2X2 만큼 체크하면 된다 
        # R, D, RD => 범위 : (0, 0) ~ (R - 2, C - 2)
        for row in range(R - 1):
            for col in range(C - 1):
                if board[row][col] == EMPTY:
                    continue
                
                # 블록 기준 4개 확인
                if is_possible(R, C, board, row, col):
                    temp.append((row, col))

        if not temp:
            break

        # 터뜨릴 블록 있을 경우 업데이트
        answer += update_board(R, C, board, temp)

    return answer

R, C = 	4, 5 
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(R, C, board))