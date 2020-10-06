# 기타리스트
# https://www.acmicpc.net/problem/1495

# 최대로 가능한 볼륨 구하는 함수
def find_max_volume(M, board):
    LAST = len(board) - 1

    for idx in range(M, -1, -1):
        if board[LAST][idx]:
            return idx

    return -1


def solution(N, S, M, volumes):
    answer = 0
    board = [[0] * (M + 1) for _ in range(N + 1)] # [N개의 곡][0 ~ MAX볼륨] 형태로 배열 구성
    board[0][S] = 1 # 최초 볼륨 check

    for song in range(N): # N개의 곡에 대해
        for volume in range(M + 1): # M개의 볼륨 탐색
            if not board[song][volume]:
                continue
            
            plus_vol = volume + volumes[song]
            minus_vol = volume - volumes[song]
            
            # 다음 곡에 대해 볼륨 갱신
            if 0 <= plus_vol <= M:
                board[song + 1][plus_vol] = 1 
            if 0 <= minus_vol <= M:
                board[song + 1][minus_vol] = 1

    answer = find_max_volume(M, board)

    return answer

# main
N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

print(solution(N, S, M, volumes))