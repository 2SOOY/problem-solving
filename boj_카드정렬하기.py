# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import heapq

def solution(cards):
    answer = 0
    heapq.heapify(cards)

    while len(cards) >= 2:
        # 최소 섞는 횟수
        # 제일 작은 카드 더미 2개를 뽑아 합친다. 
        card_1 = heapq.heappop(cards)
        card_2 = heapq.heappop(cards)

        new_card = card_1 + card_2
        answer += new_card
        heapq.heappush(cards, new_card)

    return answer

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

print(solution(cards))