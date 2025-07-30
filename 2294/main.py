import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

q = deque([(0, 0)]) # (현재 금액, 사용한 동전 개수)
visited = [False] * (k + 1)
visited[0] = True

while q:
    cur_amount, coin_count = q.popleft()

    if cur_amount == k:
        print(coin_count)
        exit()

    for coin in coins:
        next_amount = cur_amount + coin

        if next_amount <= k and not visited[next_amount]:
            visited[next_amount] = True
            q.append((next_amount, coin_count + 1))

print(-1)