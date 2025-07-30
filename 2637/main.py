import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    adj[x].append((y, k))
    indegree[y] += 1

# 각 부품을 만드는 데 필요한 기본 부품의 개수
need = [[0] * (n + 1) for _ in range(n + 1)]

# 위상 정렬을 위한 큐
q = deque()

# 진입 차수가 0인 노드들을 큐에 추가 (기본 부품들)
basic = []
for i in range(1, n + 1):
    if not adj[i]:
        basic.append(i)

    if indegree[i] == 0:
        q.append(i)
        need[i][i] = 1

# 위상 정렬 수행
while q:
    current = q.popleft()

    for next_node, count in adj[current]:
        # current로 next_node를 만들 때 필요한 기본 부품들 계산
        for i in range(1, n + 1):
            need[next_node][i] += need[current][i] * count

        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

# 완제품 n을 만드는데 필요한 기본 부품들 출력
for i in basic:
    print(i, need[i][n])
