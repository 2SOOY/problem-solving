# 공유기 설치
# https://www.acmicpc.net/problem/2110

def is_possible(HOME, WIFI, spots, mid):
    count = 1 # 공유기 설치 수 - 맨 처음 설치
    idx = 0 # 현재 설치된 공유기 위치
    
    # 거리에 따른 설치 가능 여부 확인
    for i in range(1, HOME):
        if spots[i] - spots[idx] >= mid:
            count += 1
            idx = i

            if count == WIFI:
                return True

    return False

def solution(HOME, WIFI, spots):
    spots.sort()
    answer = 0

    # 1. 공유기 2개 => 처음이랑 끝
    if WIFI == 2:
        return spots[-1] - spots[0]
    
    # 2. 이분탐색 이용
    start, end = 1, (spots[-1] - spots[0]) // (WIFI - 2)

    while start <= end:
        mid = (start + end) // 2
        if is_possible(HOME, WIFI, spots, mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
        
    return answer


HOME, WIFI = map(int, input().split())
spots = [int(input()) for _ in range(HOME)]
print(solution(HOME, WIFI, spots))