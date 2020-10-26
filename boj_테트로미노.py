# 테트로미노
# https://www.acmicpc.net/problem/14500
from copy import deepcopy

# R * C 배열 회전 함수
def rotate(board):
    R, C = len(board), len(board[0])
    result = [[0] * R for _ in range(C)] # C * R matrix

    for row in range(R):
        for col in range(C):
            result[col][R - row - 1] = board[row][col]
    
    return result

# 배열 대칭 함수
def symmetrize(borad):
    R, C = len(board), len(board[0])
    result = [[0] * C for _ in range(R)]

    for row in range(R):
        for col in range(C):
            result[row][C - col - 1] = board[row][col]
    
    return result


# 주어진 블록들
blocks = {1: [[1, 1, 1, 1]], 2: [[1, 1], [1, 1]], 3: [[1, 0], [1, 0], [1, 1]], 
        4: [[1, 0], [1, 1], [0, 1]], 5: [[1, 1, 1,], [0, 1, 0]]}


# 해당 보드판에서 최대값 찾는 함수
def calculate(board):
    answer = 0

    # 4번 회전 => 90, 180, 270, 360
    for _ in range(4):
        board = rotate(board)

        R, C = len(board), len(board[0])
        # 모든 블록에 대해서 최대값 찾기
        for _, block in blocks.items():
            BR, BC = len(block), len(block[0])
            
            for row in range(R - BR + 1):
                for col in range(C - BC + 1):

                    max_value = 0
                    for b_row in range(BR):
                        for b_col in range(BC):
                            if block[b_row][b_col] == 0:
                                continue
                            
                            max_value += board[row + b_row][col + b_col]

                    answer = max(answer, max_value)
    
    return answer


def solution(R, C, board):
    first = calculate(board)
    board = symmetrize(board) # 보드판 대칭하기
    second = calculate(board)

    return max(first, second)

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

print(solution(R, C, board))