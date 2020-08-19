# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060
from collections import defaultdict

WILD = '?'

# Trie의 노드
class Node():
    def __init__(self, key, data=None):
        self.key = key     # 한 글자
        self.data = data   # 맨 마지막 글자 => 해당 단어 저장
        self.children = {} # 다음 글자 노드
        self.count = 0     # 현재 글자를 갖고 있는 단어의 개수 

# Trie
class Trie():
    # 초기화 => 빈 head 노드 생성
    def __init__(self):
        self.head = Node(None)
    
    # 주어진 단어를 추가하는 메소드
    def insert(self, word):
        cur_node = self.head  # 시작 노드 HEAD

        for ch in word:
            # 다음 글자에 대한 노드가 없을 경우 => 추가
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            
            cur_node.count += 1
            cur_node = cur_node.children[ch] # 다음 글자 노드로 이동 
        
        # 마지막 글자 => 해당 단어 저장
        cur_node.count += 1
        cur_node.data = word
    
    # 주어진 접미사를 갖고 있는 단어가 몇개인지 반환하는 메소드
    def starts_with(self, prefix):
        cur_node = self.head
        result = 0
        
        for ch in prefix:
            # ? 전까지 접미사 파악
            if ch == WILD:
                break
            
            # 해당하는 접미사가 없을 경우
            if ch not in cur_node.children:
                return result
            
            cur_node = cur_node.children[ch]
        
        # 해당하는 접미사 있는 경우
        # 현재 노드의 count 값 => 접미사를 포함하는 단어의 개수
        return cur_node.count


def make_trie(words, tries):
    # 같은 길이를 갖는 단어끼리 트라이에 저장
    # frodo, froto => 같은 트라이
    # frodo, frodon => 다른 트라이
    for word in words:
        tries[len(word)].insert(word)

    return 

def solution(words, queries):
    answer = []

    tries = defaultdict(Trie)
    reverse_tires = defaultdict(Trie)

    reverse_words = [word[::-1] for word in words]

    make_trie(words, tries)
    make_trie(reverse_words, reverse_tires)

    for query in queries:
        query_len = len(query)
        # 모든 단어가 ?
        if query[0] == WILD and query[-1] == WILD:
            answer.append(tries[query_len].head.count)
        
        # 접두사
        elif query[-1] == WILD:
            answer.append(tries[query_len].starts_with(query))
        
        # 접미사
        else:
            answer.append(reverse_tires[query_len].starts_with(query[::-1]))


    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))