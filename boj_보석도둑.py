# 보석 도둑
# https://www.acmicpc.net/problem/1202
import heapq

WEIGHT, VALUE = 0, 1

def solution(N, K, jewelries, bags):
    answer = 0
    candidates = []
    jewelries = [(weight, -value) for weight, value in jewelries]
    heapq.heapify(jewelries) # 무게 오름차순, 가치 내림차순 heap 구성

    bags.sort() # 무게 오름차순 정렬

    for limit in bags:
        # 현재 가방의 무게를 기준으로 담을 수 있는 모든 보석 담기
        while jewelries:
            cur = heapq.heappop(jewelries)

            if cur[WEIGHT] <= limit:
                heapq.heappush(candidates, cur[VALUE])

            else:
                heapq.heappush(jewelries, cur)
                break
        
        # 해당 가방에 가장 높은 가치의 보석 담기
        if candidates:
            answer += heapq.heappop(candidates)    

    return abs(answer)

N, K = map(int, input().split())
jewelries = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
print(solution(N, K, jewelries, bags))