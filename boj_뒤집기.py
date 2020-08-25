# 뒤집기
# https://www.acmicpc.net/problem/1439

from collections import deque

# 연속되는 0 or 1 끼리 구분하는 함수
def bind_same_number(queue):
    result = []
    result.append(queue[0]) # 최초 문자열의 첫번째 성분 저장

    # queue의 pop한 문자가
    # result의 배열의 마지막 부분의 원소와 다르다면
    # result 배열에 pop한 문자열 추가
    while queue:
        number = queue.popleft()
        if number == result[-1]:
            continue

        result.append(number)

    return result


def solution(s):
    queue = deque(list(s))
    # 0001000 == 010 == 0011111000
    # 결국 연속되는 부분이 깨질 때마다 구분하는 것이 핵심
    bind_result = bind_same_number(queue)

    # 구분의 결과 0,1의 반복되는 구조이다
    # 여기서 더 적은 숫자의 개수가 뒤집을 횟수이다.
    num_one = bind_result.count('1')
    num_zero = bind_result.count('0')

    # 더 쉬운 방법은 
    # result 배열 길이의 //2 연산으로 구할 수 있음
    # 짝수면 0과 1의 개수가 같음
    # 홀수면 0과 1의 개수가 1개 차이가 남 
    
    return min(num_one, num_zero)

s = input()
print(solution(s))