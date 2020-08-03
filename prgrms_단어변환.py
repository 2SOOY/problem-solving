# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

# 단어끼리 변환이 가능한지 판별  
def is_changeable(word1, word2):
    count = 1
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count -= 1

            if count < 0:
                return False
    
    return True


def solution(begin, target, words):
    check = [False] * len(words) # 단어 사용 여부 배열
    queue = deque()
    queue.append((begin, 0)) # 단어, 변화 횟수
    
    # BFS
    while queue:
        cur_word, step = queue.popleft()

        for i in range(len(words)):
            if check[i] == False and is_changeable(cur_word, words[i]):
                if words[i] == target:
                    return step + 1

                queue.append((words[i], step + 1))
                check[i] = True
    
    return 0