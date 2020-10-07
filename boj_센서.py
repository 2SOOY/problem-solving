# 센서
# https://www.acmicpc.net/problem/2212


def solution(N, K, sensors):
    # 1. 센서 < 집중국 => 모든 구간 커버 가능 ** 주의
    if N <= K:
        return 0

    # 2. 센서 > 집중국
    sensors.sort() # 센서 좌표들 정렬 => 인접 센서들의 거리 차를 구하기 위함
    diff_sensors = []

    for idx in range(1, N):
        dist = sensors[idx] - sensors[idx - 1]
        diff_sensors.append(dist)
    
    # 거리 차가 많이 나는 부분부터 구간을 선택하면 된다.
    diff_sensors.sort()

    loop = K - 1
    while loop != 0:
        diff_sensors.pop()
        loop -= 1

    return sum(diff_sensors)

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

print(solution(N, K, sensors))