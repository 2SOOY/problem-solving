# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

# 가능한 단어인지 확인하는 함수
def is_possible(used_words, prev, cur):
    # 이미 사용된 단어 판별
    if cur in used_words:
        return False
    
    # 이어지는 단어 판별
    if prev[-1] != cur[0]:
        return False
    
    return True

def solution(n, words):
    answer = [0, 0]
    used_words = set() # 사용된 단어
    used_words.add(words[0]) # 최초 단어 추가
    turn = 1 # 현재 라운드
    
    for idx in range(1, len(words)):
        person = (idx % n) + 1
        prev_word = words[idx - 1]
        cur_word = words[idx]
        
        if person == 1: # 첫번째 사람 => 턴 갱신
            turn += 1
        
        if is_possible(used_words, prev_word, cur_word):
            used_words.add(cur_word) # 새로운 단어 추가
            continue
        
        # 게임 종료
        return [person, turn]
    
    # 게임 성공
    return answer

