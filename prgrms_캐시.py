# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

HIT, MISS = 1, 5

def solution(cache_size, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    cache = deque()

    if cache_size == 0:
        return len(cities) * MISS

    for city in cities:
        if city in cache:
            cache = deque([c for c in cache if city != c])
            cache.append(city)
            answer += HIT
        
        else:
            if len(cache) == cache_size:
                cache.popleft()

            cache.append(city)
            answer += MISS

    return answer

cache_size = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cache_size, cities))