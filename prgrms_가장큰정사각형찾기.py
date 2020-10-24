# 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0
    R, C = len(board), len(board[0])
    
    # 1 x N or N x 1 형태의 사각형
    if R == 1 or C == 1:
        for row in range(R):
            for col in range(C):
                if board[row][col] == 1:
                    return 1
        return 0
    
    # R * C의 사각형 => DP
    for row in range(1, R):
        for col in range(1, C):
            # (1, 1) 부터 시작
            if board[row][col] == 0:
                continue
            
            # 현재 위치에서 구할 수 있는 최대 길이의 정사각형
            # L, U, LU의 좌표 중 최소값 + 1
            # 다만 본인이 0일 경우 pass
            min_val = min(board[row - 1][col], board[row][col - 1], board[row - 1][col - 1])
            board[row][col] = min_val + 1
            
            answer = max(board[row][col], answer) # 정사각형 최대길이 갱신
            
    return answer ** 2

# board = [[0], [1] ,[1], [1], [1], [1]]
board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))
