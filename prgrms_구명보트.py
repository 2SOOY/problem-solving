# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left <= right:
        # 최소 구명보트 => 가장 무거운 사람 + 가장 가벼운 사람
        # 왜냐하면 2명이라는 제한 사항이 존재한다.
        # 만약, 보트가 명수 제한없이 무게제한만 있었다면 무거운 사람부터 태우는 방식으로 바꿔야함
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        
        else:
            right -= 1
        
        answer += 1
    
    return answer


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))