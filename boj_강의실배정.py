# 강의실 배정
# https://www.acmicpc.net/problem/11000
import heapq

START, FINISH = 0, 1

def soluition(N, classes):
    answer = 0
    # 수업 시작이 빠른 순으로 정렬, 시작이 같다면 끝나는 시간이 이른 순서대로 정렬
    classes.sort(key= lambda x: (x[START], x[FINISH]))

    queue = []
    first_class = classes[0]
    # 힙에 추가시 수업이 끝나는 시간을 우선으로 추가
    # 현재 가장 빨리 끝나는 수업을 통해 다음 수업의 교실을 추가할지 말지 파악할 수 있기 때문
    heapq.heappush(queue, (first_class[FINISH] , first_class[START]))


    for idx in range(1, N):
        cur_end, _ = queue[0] # 가장 빨리 끝나는 수업
        temp_start, temp_end = classes[idx] # 다음 수업

        # 현재 수업 끝나는 시간 <= 다음 수업 시작 => 현재 교실 이어서 사용 가능
        # 현재 수업 없애기
        if cur_end <= temp_start:
            heapq.heappop(queue)
        
        heapq.heappush(queue, (temp_end, temp_start))
    
    answer = len(queue)
    return answer

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
print(soluition(N, classes))