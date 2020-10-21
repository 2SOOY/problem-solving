# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
from copy import deepcopy

BLACK, WHITE = 'B', 'W'

# 색 바꾸기
def toggle(color):
    info = {BLACK: WHITE, WHITE: BLACK}
    return info[color]

# 다시 칠해야하는 숫자를 계산하는 함수
def count_paint(chess_board):
    answer = 0
    chess_board = deepcopy(chess_board)

    for row in range(8):
        for col in range(8):
            # (0, 0) 패스
            if row == 0 and col == 0:
                continue
            
            cur_color = chess_board[row][col] # 현재 위치의 색
            left = col - 1 # 왼쪽 col 좌표
            up = row - 1 # 위쪽 row 좌표

            # 0번 row에 해당하는 경우 => 왼쪽만 비교
            if row == 0:
                left_color = chess_board[row][left]
                if left_color == cur_color:
                    answer += 1
                    chess_board[row][col] = toggle(cur_color)

                continue

            # 0번 col에 해당하는 경우 => 위쪽만 비교
            if col == 0:
                up_color = chess_board[up][col]
                if up_color == cur_color:
                    answer += 1
                    chess_board[row][col] = toggle(cur_color)
                
                continue
            
            # 왼쪽, 위쪽 모두 비교
            left_color = chess_board[row][left]
            up_color = chess_board[up][col]

            if left_color == cur_color:
                answer += 1
                chess_board[row][col] = toggle(cur_color)

    return answer

def solution(R, C, board):
    answer = R*C

    for row in range(R - 8 + 1):
        for col in range(C - 8 + 1):
            temp_chess_board = [board[row + i][col: col + 8] for i in range(8)]

            # 체스판의 (0, 0)을 그대로 사용했을 때, 최소값 
            answer = min(answer, count_paint(temp_chess_board))

            # 체스판의 (0, 0)을 바꿨을 때, 최소값
            temp_chess_board[0][0] = toggle(temp_chess_board[0][0])
            answer = min(answer, count_paint(temp_chess_board) + 1)

    return answer

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
print(solution(R, C, board))