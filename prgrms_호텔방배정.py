# 호텔 방 배정
# https://programmers.co.kr/learn/courses/30/lessons/64063

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)  # 효율성 테스트를 위한 재귀 깊이 조정


def find_empty_room(rooms, num):
    parent = rooms[num]
    # 빈 방 X
    if parent:
        root_num = find_empty_room(rooms, parent)  # 루트 노드 탐색
        rooms[parent] = root_num + 1
        return root_num

    # 빈 방
    else:
        rooms[num] = num + 1
        return num


def solution1(k, room_number):
    answer = []
    rooms = defaultdict(int)

    for num in room_number:
        answer.append(find_empty_room(rooms, num))

    return answer


def solution2(k, room_number):
    answer = []
    rooms = dict()

    for num in room_number:
        # 빈 방 X
        if num in rooms:
            visited = [num]  # 방 탐색 히스토리 => 방들의 부모 노드 업데이트 하기 위함
            parent = rooms[num]

            while parent in rooms:  # 루트 노드가 나올 때까지 탐색
                visited.append(parent)
                parent = rooms[parent]

            # 지금까지 탐색한 모든 방들 루트 노드 + 1로 업데이트
            for visited_num in visited:
                rooms[visited_num] = parent + 1

            # 루트 노드 방 배정
            answer.append(parent)
            rooms[parent] = parent + 1

        # 빈 방
        else:
            answer.append(num)
            rooms[num] = num + 1

    return answer


k = 10
room_number = [1, 2, 1, 5, 3, 1, 2]
print(solution1(k, room_number))
print(solution2(k, room_number))
