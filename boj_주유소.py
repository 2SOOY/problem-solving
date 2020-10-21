# 주유소
# https://www.acmicpc.net/problem/13305

def solution(N, distances, prices):
    answer = 0

    if N == 2:
        return distances[0] * prices[0]
    
    min_price = max(prices[:-1]) # 현재 기준 가장 낮은 주유소의 가격
    
    for i in range(N - 1):
        dist = distances[i] # 다음 주유소 이동할 거리
        price = prices[i]   # 현재 주유소 가격

        # 현재 기준으로 가격이 더 낮은 주유소 등장 시 최저가 갱신
        if price <= min_price:
            min_price = price
        
        answer += (dist * min_price) # 최저가를 기준으로 계산
    
    return answer


N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
print(solution(N, distances, prices))