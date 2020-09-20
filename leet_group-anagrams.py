# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

def groupAnagrams(strs):
    result = []
    anagram_dict = defaultdict(list)

    # 요소가 1개만 존재할 경우
    if len(strs) == 1:
        result.append(strs)
        return result

    # 요소 여러개
    # 정렬 & 딕셔너리 이용 **
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    
    for words in anagram_dict.values():
        result.append(words)      

    return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))