# BOJ 1432 - 그래프 수정
# 위상 정렬(Topological Sort)을 이용한 문제 해결
# 시간복잡도: O(V^2 + VlogV) - V는 정점의 개수

import sys
import heapq

input = sys.stdin.readline

# [입력 처리] 정점의 개수 입력
n = int(input())

# [입력 처리] 인접 행렬 입력 - 각 행을 문자별로 분리하여 정수 배열로 변환
adj = [[int(c) for c in input().strip()] for _ in range(n)]

# [데이터 구조 초기화] 각 정점의 out-degree(나가는 간선의 개수) 계산
outdegree = [0] * n
for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:  # i에서 j로 가는 간선이 존재하면
            outdegree[i] += 1

# [데이터 구조 초기화] 결과를 저장할 배열
result = [0] * n

# [알고리즘 핵심 로직] 위상 정렬을 위한 최대 힙 초기화
# out-degree가 0인 정점들을 힙에 추가 (음수로 저장하여 최대 힙 구현)
heap = []
for i in range(n):
    if outdegree[i] == 0:  # 나가는 간선이 없는 정점
        heapq.heappush(heap, -i)  # 가장 큰 번호부터 처리하기 위해 음수로 저장

# [알고리즘 핵심 로직] 위상 정렬 수행
# 가장 큰 번호부터 차례대로 할당
num = n
while heap:
    # 현재 처리할 정점 (가장 큰 번호)
    current = -heapq.heappop(heap)
    result[current] = num  # 현재 정점에 번호 할당
    num -= 1
    
    # 현재 정점으로 들어오는 모든 간선 제거
    for i in range(n):
        if adj[i][current] == 1:  # i에서 current로 가는 간선이 있으면
            outdegree[i] -= 1  # i의 out-degree 감소
            if outdegree[i] == 0:  # out-degree가 0이 되면 힙에 추가
                heapq.heappush(heap, -i)

# [출력 처리] 결과 출력
if num > 0:  # 모든 정점을 처리하지 못한 경우 (사이클 존재)
    print(-1)
else:  # 성공적으로 위상 정렬 완료
    print(*result)