from collections import deque

N = int(input())

card = deque([i for i in range(1, N + 1)])

while len(card) > 1:
    badak = card.popleft()
    gotoback = card.popleft()
    card.append(gotoback)

print(card[0])

