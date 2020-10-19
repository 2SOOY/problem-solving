# 수리공 항승
# https://www.acmicpc.net/problem/1449
import heapq

def solution(N, L, holes):
    answer = 1
    heapq.heapify(holes)
    cur = heapq.heappop(holes)

    while holes:
        temp = heapq.heappop(holes)
        # 테이프 붙이기 가능
        if temp - cur <= L - 1:
            continue
        
        # 테이프 붙일 수 없을 때
        cur = temp
        answer += 1

    return answer

N, L = map(int, input().split())
holes = list(map(int, input().split()))

print(solution(N, L, holes))