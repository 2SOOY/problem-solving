# 설탕 배달
# https://www.acmicpc.net/problem/2839
MAX = 5000

def solution(N):
    weights = [-1] * (MAX + 1) # 각 무게에 필요한 최소 봉지수
    weights[3] = 1 # 3, 5에 대해선 봉지 1개씩 필요
    weights[5] = 1

    # DP
    for i in range(3, N + 1):
        # 현재 무게 기준 3g을 채웠을 때랑 5g을 채웠을 때 최소 봉지수 가져오기
        temp1 = weights[i - 3]
        temp2 = weights[i - 5]

        if temp1 == -1 and temp2 == -1:
            continue

        if temp1 == -1:
            temp1 = MAX
        
        if temp2 == -1:
            temp2 = MAX
        
        # 가능한 봉지 개수 중 최소값 갱신하기
        weights[i] = min(temp1, temp2) + 1

    return weights[N]

N = int(input())
print(solution(N))