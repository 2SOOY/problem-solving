# 도서관
# https://www.acmicpc.net/problem/1461

def find_distance(M, books):
    answer = 0

    books.sort(reverse=True) # 멀리 있는 책부터 옮기기 위해 정렬 (최소 이동 거리)
    # M권씩 책 들기 및 왕복 이동
    for idx in range(0, len(books), M):
        temp = books[idx: idx + M] # M 등분
        answer += 2 * max(temp) # 왕복거리

    return answer

def solution(N, M, books):
    answer = 0

    plus_books = []
    minus_books = []

    # 1. +, - 분리
    for book in books:
        if book > 0:
            plus_books.append(book)
        else:
            minus_books.append(-book)
    
    # 2. +, - 파트 각각 이동거리 구하기 (왕복)
    max_plus = 0
    max_minus = 0

    if plus_books:
        max_plus = max(plus_books)
        answer += find_distance(M, plus_books)
    
    if minus_books:
        max_minus = max(minus_books)
        answer += find_distance(M, minus_books)
    
    # 3. 최종 움직일 편도 거리 구하기
    max_dist = max(max_plus, max_minus)
    answer -= max_dist

    return answer

N, M = map(int, input().split())
books = list(map(int, input().split()))

print(solution(N, M, books))