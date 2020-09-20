# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


# 방법1 - 단순 반복
def longestPalindrome(s):
    max_len = 0
    result = ''
    if len(s) == 1:
        return s

    for start in range(len(s)):
        for end in range(start, len(s)):
            temp_word = s[start: end + 1]
            if temp_word != temp_word[::-1]:
                continue

            if max_len < len(temp_word):
                max_len = len(temp_word)
                result = ''.join(temp_word)

    return result


# 방법2 - 투포인터 사용
# 펠린드롬을 만족할때마다 확장시키는 함수
def expand_word(s, left, right):
    result = ''

    while left >= 0 and right < len(s) and s[left] == s[right]:
        result = s[left: right + 1]
        left -= 1
        right += 1

    return result


def longestPalindrome2(s):
    result = ''

    if len(s) < 2:
        return s

    for start in range(len(s)):
        word_one = expand_word(s, start, start)     # 1글자 word에 대해 펠린드롬 구하기
        word_two = expand_word(s, start, start + 1) # 2글자 word에 대해 펠린드롬 구하기

        result = max(word_one, word_two, result, key=len) # 가장 긴 펠린드롬 단어 갱신

    return result


s = "babad"
print(longestPalindrome(s))
print(longestPalindrome2(s))