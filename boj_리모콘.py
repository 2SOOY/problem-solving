# 리모콘
# https://www.acmicpc.net/problem/1107

START = 100
MAX = 1000000 # 1,000,000인 이유 => 버튼이 9만 가능 & target = 500,000 

# +(-)버튼만 사용해서 채널까지 이동하는 경우
def get_only_plus(target):
    return abs(target - START)

def solution(buttons, target):
    answer = MAX
    # 모든 버튼이 고장난 경우
    if len(buttons) == 10:
        return get_only_plus(target)

    # n번에서 target을 만드는데 필요한 클릭 수 구하기
    for number in range(MAX):
        str_number = str(number)
        
        is_possible = True
        for num in str_number:
            # 고장난 버튼이 있을 경우 => 다음 숫자 탐색
            if buttons and int(num) in buttons:
                is_possible = False
                break
        
        # 해당 번호를 만들 수 있는 경우
        # 해당 번호의 길이 + 목표 채널과의 차이값
        if is_possible:
            temp_answer = len(str_number) + abs(number - target)
            answer = min(answer, temp_answer)

    # 100번부터 시작해서 변환하는 것과 비교하기
    answer = min(answer, get_only_plus(target))

    return answer

# 런타임 에러 주의 *
target = int(input())
k = int(input())
if k != 0:
    buttons = list(map(int, input().split()))
    print(solution(buttons, target))
else:
    buttons = []
    print(solution(buttons, target))
    
    