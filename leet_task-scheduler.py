# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from collections import Counter, defaultdict
import heapq

def leastInterval(tasks, n):
    number_of_tasks = Counter(tasks)
    sorted_tasks = number_of_tasks.most_common() # 개수가 많은 순서대로 정렬 [('TASK', NUMBER), ... ] 구조

    max_number = sorted_tasks[0][1] # task 중에서 가장 많은 작업의 수
    max_tasks = 0 # 최대 개수를 갖는 task의 수 => 최대 수가 여러개 있을 경우

    # 최대 개수를 갖는 task의 개수 구하기
    for task, number in sorted_tasks:
        if max_number == number:
            max_tasks += 1  

    # max_number = 3, max_tasks = 2, n = 3
    # AB__AB__AB : 형태로 구해짐
    # AB__AB__ => (max_tasks - 1) * (n + 1)
    #         AB => max_tasks
    total_time = (max_number - 1) * (n + 1) + max_tasks

    return max(total_time, len(tasks))


def leastInterval2(tasks, n):
    task_info = Counter(tasks)
    heap = []

    # max heap 구성하기
    for task, number in task_info.items():
        heapq.heappush(heap, [-number, task])
    
    total_time = 0 # 총 소요 시간

    # 시뮬레이션 by그리디
    while heap:
        i, temp_list = 0, [] # unit time, 힙에 다시 추가할 task를 담은 배열
        
        # 1개의 작업당 unit time동안 처리할 수 없음
        while i <= n:
            total_time += 1

            # 작업이 있는 경우
            if heap:
                number, task = heapq.heappop(heap)

                # 작업 한개 처리 후 임시 리스트에 추가
                if number != -1:
                    temp_list.append([number + 1, task])
            
            # 더 이상 남아있는 작업이 없다면 => 완료
            if not heap and not temp_list:
                break

            # unit time 측정
            i += 1
        
        # 작업 처리 후 남아있는 작업들 다시 힙에 추가하여 시뮬레이션 진행 
        for item in temp_list:
            heapq.heappush(heap, item)

    return total_time

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval2(tasks, n))
