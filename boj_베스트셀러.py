# 베스트셀러
# https://www.acmicpc.net/problem/1302

def solution(N, books):
    result = []
    books_info = {}

    # 1. 개수 세기
    for book in books:
        if book not in books_info:
            books_info[book] = 1
        else:
            books_info[book] += 1
    
    best_seller_num = max(books_info.values())

    # 2. 가장 많은 개수 파악 후 => 사전순 정렬
    for book, num in books_info.items():
        if num == best_seller_num:
            result.append(book)
            continue

    result.sort()
    return result[0] 

N = int(input())
books = [input() for _ in range(N)]
print(solution(N, books))