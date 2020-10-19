# 과제
# https://www.acmicpc.net/problem/13904
import heapq

DAY, SCORE = 0, 1

# 풀이 1. 컵라면(1781) 문제와 풀이 동일 => heap 이용
# heap의 원소 개수와 현재 시간과 비교하기
# 데드라인 기준으로 오름차순 정렬
def solution(N, problems):
    answer = 0
    problems.sort(key=lambda x: (x[DAY], -x[SCORE]))
    
    heap = []

    for i in range(N):
        cur = problems[i]
        heapq.heappush(heap, cur[SCORE])

        while len(heap) > cur[DAY]:
            heapq.heappop(heap)      
    
    answer = sum(heap)
    return answer 


# 풀이 2. 날짜별 table 만든 후 score 배치
# 점수를 기준으로 내림차순 정렬 => 최대한 많은 점수를 받기 위함
# 높은 점수 -> 해당 하는 날짜부터 역순으로 탐색
def solution2(N, problems):
    answer = 0
    problems.sort(key=lambda x: -x[SCORE]) # 점수를 기준으로 오름차순 정렬
    last_day = max([day for day, _ in problems]) # 각 day에 얻을 수 있는 점수를 나타낼 table

    scores = [0] * (last_day + 1)

    # 최대 점수부터 탐색
    for i in range(N):
        cur_problem = problems[i]

        # 최대 점수를 얻을 수 있는 day기준으로 역순으로 탐색
        # 역순으로 하는 이유 => 나중에 풀 수 있는 문제는 초반에도 풀 수 있음 => 초반에 풀 수 있는 문제를 남겨놓기 위함
        for j in range(cur_problem[DAY], 0, -1):
            if scores[j] == 0:
                scores[j] = cur_problem[SCORE]
                break

    answer = sum(scores)
    
    return answer

N = int(input())
problems = [tuple(map(int, input().split())) for _ in range(N)]
print(solution2(N, problems))