# 트라이

# Node 클래스
class Node():
    def __init__(self, key, data=None):
        self.key = key      # 글자
        self.data = data    # 마지막 글자 => 해당 단어
        self.children = {}  # 다음 글자 Node들을 담을 dict


# Trie 클래스
class Trie():
    def __init__(self):
        self.head = Node(None) # 빈 HEAD 노드 생성

    # 단어를 트라이에 추가하는 메소드
    def insert(self, word):
        cur_node = self.head # 시작 => HEAD

        # 글자 별로 탐색
        # 해당 글자 없으면 => children에 글자 노드 추가
        # 이후 다음 글자 노드로 이동
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            cur_node = cur_node.children[ch]
        
        # 마지막 글자에 대해서는 해당 단어 정보 추가
        cur_node.data = word
    
    # 해당 단어를 갖고있는지 파악하는 메소드
    def is_searched(self, word):
        cur_node = self.head

        for ch in word:
            if ch not in cur_node.children:
                return False    
            
            cur_node = cur_node.children[ch]
        
        if cur_node.data == word:
            return True

    # 주어진 prefix로 시작하는 모든 단어들을 반환하는 메소드
    def starts_with(self, prefix):
        cur_node = self.head
        result = []

        # prefix 까지 탐색
        for ch in prefix:
            if ch not in cur_node.children:
                return result

            cur_node = cur_node.children[ch]
        
        # DFS를 이용하여 모든 children을 탐색
        # 모든 단어들을 result 배열에 추가
        stack = list(cur_node.children.values())
        while stack:
            node = stack.pop()

            if node.data != None:
                result.append(node.data)
            
            stack += list(node.children.values())
        
        return result


trie = Trie()
words = ["frodo", "front", "frost", "frozen", "frame", "friend", "fly"]

for word in words:
    trie.insert(word)

print(trie.is_searched('frodo'))   # True
print(trie.is_searched('frodu'))   # False
print(trie.is_searched('frozen'))  # True
print(trie.is_searched('flying'))  # False

print(trie.starts_with('fr')) # ['friend', 'frame', 'frozen', 'frost', 'front', 'frodo']
print(trie.starts_with('fro')) # ['frozen', 'frost', 'front', 'frodo']
print(trie.starts_with('fl')) # ['fly']