# 단어 수학
# https://www.acmicpc.net/problem/1339

# 자리수를 고려하여 각 알파벳의 가중치 구하기
# ABAA => A: 1011, B: 100
def get_scores(words):
    scores = dict()

    for word in words:
        for i, char in enumerate(word):
            num = len(word) - i - 1 # 제곱수
            
            if char not in scores:
                scores[char] = (10 ** num)
                continue

            scores[char] += (10 ** num)
    
    # 정렬하기
    temp = []
    for char, value in scores.items():
        temp.append((value, char))
    
    temp.sort(reverse=True) # score 내림차순 정렬
    
    return temp


# 주어진 문자단어를 매핑된 숫자에 맞춰 계산하기
def calculate(transform_info, words):
    answer = 0

    for word in words:
        temp = 0
        for char in word:
            temp = (10 * temp) + transform_info[char]
        
        answer += temp
    
    return answer


def solution(N, words):
    answer = 0
    transform_info = dict()

    scores = get_scores(words)

    # 가중치가 높은 알파벳별로 9부터 할당하기
    for i in range(len(scores)):
        alphabet = scores[i][1]
        transform_info[alphabet] = 9 - i

    answer = calculate(transform_info, words)
    return answer


N = int(input())
words = [input() for _ in range(N)]
print(solution(N, words))