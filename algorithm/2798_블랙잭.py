import sys
import itertools
read = sys.stdin.readline

N, M = map(int, read().split())
cardList = list(map(int, read().split()))
answer = 0

for cards in itertools.combinations(cardList, 3):
    cardSum = sum(cards)
    if answer < cardSum <= M:
        answer = cardSum

print(answer)
