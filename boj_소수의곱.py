# 소수의 곱
# https://www.acmicpc.net/problem/2014
import heapq

MAX = 2 ** 32

def solution(primes, K):
    checked = set()
    heap = primes[:]
    answer = 0
    i = 0 # K 번째 숫자가 나올 때까지 증가시킬 숫자

    # 힙의 성질 => 제일 작은(큰) 숫자를 추출할 수 있음
    # K번 추출하면 K번째 숫자를 구할 수 있음
    while i < K:
        num = heapq.heappop(heap)

        # 중복 체크
        if num in checked:
            continue
        
        # 없는 숫자 => 추가 및 i번째 증가
        answer = num
        checked.add(num)
        i += 1
        
        # 나온 숫자에 대해서 기존 primes 배열의 소수들과 곱해서 힙에 추가
        for prime in primes:
            temp = num * prime
            if temp >= MAX:
                continue

            heapq.heappush(heap, num * prime)            

    return answer

N, K = map(int, input().split())
primes = list(map(int, input().split()))
print(solution(primes, K))