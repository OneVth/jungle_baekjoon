# BOJ 4803 - 트리
# 알고리즘: Union-Find (Disjoint Set) + 사이클 검출
# 시간복잡도: O(m * α(n)) (α는 아커만 함수의 역함수)

import sys

input = sys.stdin.readline

# Union-Find의 Find 연산: 경로 압축 최적화 포함
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축으로 트리 높이 최소화
    return parent[x]

# Union-Find의 Union 연산: 랭크 기반 합집합
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        # 서로 다른 집합이므로 합치기 (랭크 기반 최적화)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True  # 성공적으로 합쳐짐 (사이클 없음)
    return False     # 이미 같은 집합 (사이클 발생)


# 테스트 케이스 번호 초기화
case_num = 1

# 입력 처리: 무한 루프로 여러 테스트 케이스 처리
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:  # 종료 조건
        break

    # 데이터 구조 초기화
    parent = [i for i in range(n + 1)]    # 각 노드의 부모 (자기 자신으로 초기화)
    rank = [0] * (n + 1)                  # 각 트리의 랭크 (높이 추정치)
    has_cycle = [False] * (n + 1)         # 각 연결 컴포넌트의 사이클 여부

    # 핵심 알고리즘: 간선 처리 및 사이클 검출
    for _ in range(m):
        u, v = map(int, input().split())
        if not union(parent, rank, u, v):
            # Union 실패 = 사이클 발생
            root = find(parent, u)  # 사이클이 발생한 연결 컴포넌트의 루트
            has_cycle[root] = True

    # 트리 개수 계산: 사이클이 없는 연결 컴포넌트만 카운트
    trees = set()
    for i in range(1, n + 1):
        root = find(parent, i)              # 각 노드가 속한 연결 컴포넌트의 루트 찾기
        if not has_cycle[root]:             # 사이클이 없는 컴포넌트만
            trees.add(root)                 # 루트를 집합에 추가 (중복 제거)

    # 결과 출력: 트리 개수에 따른 메시지 출력
    tree_count = len(trees)
    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")

    case_num += 1