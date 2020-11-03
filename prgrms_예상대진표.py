# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

# 비효율적 풀이
# 모든 배열의 성분값을 업데이트
def solution1(n,a,b):
    count = 1
    roots = [i for i in range(n + 1)]

    while roots[a] != roots[b]:
        # 모든 성분에 대해 2^count 크기만큼
        for i in range(1, n + 1, 2**count):
            # root값을 업데이트함
            for j in range(i, i + 2**count):
                roots[j] = i
        
        count += 1

    return count - 1


# 효율적 풀이
# 문제에 주어진 예시를 적극 활용하기
def solution2(n, a, b):
    answer = 0

    while a != b:
        # 다음 라운드에 변환될 숫자로 업데이트 진행
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer

n = 16
a = 2
b = 4
print(solution2(n, a, b))