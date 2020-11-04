# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
import math

# 각 작업의 완료 시간을 구하는 함수
def get_completed_day(progresses, speeds):
    result = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]

    return result

def solution(progresses, speeds):
    answer = []
    completed_jobs = get_completed_day(progresses, speeds)
    max_day = completed_jobs[0] # 기준값

    temp_jobs = 0 # 한꺼번에 처리하는 작업의 수
    for day in completed_jobs:
        if max_day >= day:
            temp_jobs += 1
            continue
        
        # 기준 값보다 증가하는 시점 => 새롭게 배포 및 값 갱신
        answer.append(temp_jobs)
        max_day = day 
        temp_jobs = 1 
    
    if temp_jobs:
        answer.append(temp_jobs)

    return answer

progresses = [90, 55, 55]
speeds = [1, 5, 5]
print(solution(progresses, speeds))