# 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
from collections import defaultdict

def solution(N, K, orders):
    answer = 0

    # 멀티탭 구멍 충분 
    if N >= K:
        return answer

    used_items = set() # 현재 멀티탭 상태
    for i in range(K):
        item = orders[i]
        # 사용하려는 아이템이 멀티탭에 존재하는 경우
        if item in used_items:
            continue

        # 멀티탭에 사용할 자리가 있는 경우
        if len(used_items) < N:
            used_items.add(item)
            continue
        
        # 무언가 뽑아야할 경우 
        # => 1순위. 더 이상 사용하지 않을 아이템 뽑기
        # => 2순위. 사용할 아이템이 있다면 가장 나중에 사용할 아이템 뽑기

        next_idx_info = defaultdict(int) # 현재 사용중인 아이템이 추후에 언제 사용되는지 정보를 담고있는 딕셔너리
        list_used_items = list(used_items)
        
        # 딕셔너리 정보 초기화
        for j in range(N):
            cur = list_used_items[j]
            next_idx_info[cur] = 0
        
        # 다음 사용할 아이템들에 대해서 탐색
        for j in range(i + 1, K):
            temp_item = orders[j]
            # 현재 사용하는 아이템 중 가장 가까운 미래에 사용되는 시점 업데이트
            if temp_item in next_idx_info and next_idx_info[temp_item] == 0:
                next_idx_info[temp_item] = j
        
        last_idx = 0

        for cur, idx in next_idx_info.items():
            # 더 이상 사용 X => 바로 뽑기
            if idx == 0:
                used_items.remove(cur)
                break

            # 제거할 아이템 갱신
            last_idx = max(last_idx, idx)
        
        # 멀티탭에 자리가 없다면 => 마지막에 사용될 아이템 뽑기
        if len(used_items) == N:
            used_items.remove(orders[last_idx])

        # 현재 사용할 아이템 추가
        answer += 1
        used_items.add(item)

    return answer

N, K = map(int, input().split())
orders = list(map(int, input().split()))
print(solution(N, K, orders))