# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059


# 시계방향 90도 회전 함수
def rotate(key):
    N = len(key)
    result = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            result[col][N-row-1] = key[row][col]

    return result

def make_empty_board(size):
    return [[0] * size for _ in range(size)]

def solution(key, lock):
    answer = True
    KEY_SIZE, LOCK_SIZE = len(key), len(lock)
    SIZE = 2*KEY_SIZE + LOCK_SIZE - 2

    # 4방향 => 90, 180, 270, 360
    for _ in range(4):
        # key 회전
        key = rotate(key)

        # 탐색
        for row in range(SIZE - KEY_SIZE + 1):
            for col in range(SIZE - KEY_SIZE + 1):

                answer = True
                board = make_empty_board(SIZE)

                # 빈 행렬에 key 채워 넣기
                for k_row in range(KEY_SIZE):
                    for k_col in range(KEY_SIZE):
                        board[row + k_row][col + k_col] = key[k_row][k_col]

                # key로 채워진 행렬과 lock 비교하기 XOR
                # 다르면 1 / 같으면 0
                for l_row in range(LOCK_SIZE):
                    for l_col in range(LOCK_SIZE):
                        if board[KEY_SIZE - 1 + l_row][KEY_SIZE - 1 + l_col] ^ lock[l_row][l_col]:
                            continue
                        answer = False
                
                # 열릴 수 있는가 판단
                if answer:
                    return answer

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))