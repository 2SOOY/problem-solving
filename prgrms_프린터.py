# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque([(priority, num) for num, priority in enumerate(priorities)]) # 우선순위, 문서번호 형태로 변환

    while priorities:
        max_priority = max([priority for priority, _ in priorities]) # 현재 대기 문서 중 가장 높은 우선순위
        priority, num = priorities.popleft()

        # 나보다 높은 우선순위가 존재한다면 => 맨 뒤로
        if priority < max_priority:
            priorities.append((priority, num))
            continue
        
        # 내가 제일 높다 => 인쇄하기
        answer += 1
        # 해당 문서가 내가 찾는 문서 => 정답
        if num == location:
            return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))

