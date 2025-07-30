import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())  # 도시 개수
m = int(input())  # 도로 개수

# 그래프와 역방향 그래프
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))
    indegree[b] += 1
start, end = map(int, input().split())

# 1단계: 위상정렬로 최대 도달 시간 계산
queue = deque()
distance = [0] * (n + 1)

# 시작 도시 초기화
queue.append(start)
while queue:
    current = queue.popleft()
    for next_city, time in graph[current]:
        distance[next_city] = max(distance[next_city], distance[current] + time)
        indegree[next_city] -= 1
        if indegree[next_city] == 0:
            queue.append(next_city)

# 2단계: 역추적으로 임계경로 간선 개수 계산
visited = [False] * (n + 1)
critical_edges = 0
def backtrack(city):
    global critical_edges
    if visited[city]:
        return
    visited[city] = True
    for prev_city, time in reverse_graph[city]:

        # 임계경로에 포함된 간선인지 확인
        if distance[prev_city] + time == distance[city]:
            critical_edges += 1
            backtrack(prev_city)

backtrack(end)
print(distance[end])    # 최대 도달 시간
print(critical_edges)   # 임계경로 간선 개수