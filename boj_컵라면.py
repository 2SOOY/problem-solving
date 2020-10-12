# 컵라면
# https://www.acmicpc.net/problem/1781
import heapq

DEAD, CUP, NUM = 0, 1, 2

def solution(N, info):
    info.sort(key=lambda x: x[DEAD]) # deadline이 이른 순서대로 정렬
    heap = []

    for problem in info:
        cur_deadline = problem[DEAD] # 기준 deadline
        heapq.heappush(heap, problem[CUP]) # 일단 heap에 추가

        # 현재 deadline 기준 선택할 수 있는 것들이 여러개 
        # => 컵라면 적은 것들 버리기
        if cur_deadline < len(heap):
            heapq.heappop(heap)

    # heap에는 deadline을 만족하면서
    # 컵라면을 많이 받을 수 있는 문제들만 남아있음
    
    return sum(heap)

N = int(input())
info = []
for i in range(N):
    deadline, cup = map(int, input().split())
    temp = (deadline, cup, i + 1)
    info.append(temp)

print(solution(N, info))
