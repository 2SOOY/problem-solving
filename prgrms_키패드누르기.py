# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]


# 각 번호에 대한 row, col 매핑 함수
def get_location_info(keypad):
    R, C = len(keypad), len(keypad[0])
    button_info = dict()

    for row in range(R):
        for col in range(C):
            button_info[keypad[row][col]] = (row, col)

    return button_info


# 시작과 끝점 사이의 거리 계산 함수
def calculate_distance(src, dst, button_info):
    src_row, src_col = button_info[src]
    dst_row, dst_col = button_info[dst]

    distance = abs(src_row - dst_row) + abs(src_col - dst_col)

    return distance


def solution(numbers, hand):
    answer = ''
    button_info = get_location_info(keypad)
    LEFT, RIGHT = 0, 1
    hands = ['*', '#']  # 초기 손위치

    for number in numbers:
        _, col = button_info[number]
        if col == 0:
            answer += 'L'
            hands[LEFT] = number
        elif col == 2:
            answer += 'R'
            hands[RIGHT] = number
        else:
            left_dist = calculate_distance(hands[LEFT], number, button_info)
            right_dist = calculate_distance(hands[RIGHT], number, button_info)

            if left_dist == right_dist:
                if hand == 'left':
                    answer += 'L'
                    hands[LEFT] = number
                else:
                    answer += 'R'
                    hands[RIGHT] = number
            else:
                if left_dist < right_dist:
                    answer += 'L'
                    hands[LEFT] = number
                else:
                    answer += 'R'
                    hands[RIGHT] = number

    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

print(solution(numbers, hand))
