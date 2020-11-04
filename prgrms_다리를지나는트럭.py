# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 소요 시간
    bridge = deque() # 현재 다리 위에 트럭이 놓인 상태
    truck_weights = deque(truck_weights) # queue 구조로 다리를 건너므로 deque 사용

    # 트럭 보내기
    while truck_weights:
        answer += 1

        # 다리가 비었다면 트럭 추가
        if not bridge:
            truck = truck_weights.popleft()
            bridge.append((truck, answer))
            continue
        
        # 가장 오래된 트럭 다리 건너기 판단
        aged = bridge[0][1]
        if answer - aged == bridge_length:
            bridge.popleft()
        
        # 건넌 이후의 다리에 대해 트럭 추가 판단
        cur_weight = sum([w for w, _ in bridge])
        if cur_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append((truck, answer))

    # 다리 위에 존재하는 트럭에 대해 소요시간 파악
    while bridge:
        answer += 1
        if answer - bridge[0][1] == bridge_length:
            bridge.popleft() 

    return answer


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))