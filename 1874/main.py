# BOJ 1874 - 스택 수열
# 알고리즘: 스택 시뮬레이션
# 시간복잡도: O(n)

import sys

input = sys.stdin.readline

# 입력 처리: 수열의 길이 n 읽기
n = int(input())

# 목표 수열 입력받기
seq = []
for _ in range(n):
    seq.append(int(input()))

# 데이터 구조 초기화
stack = []          # 스택: 1부터 n까지 순서대로 push할 스택
result = []         # 결과: push(+)와 pop(-) 연산 기록
cur = 0             # 현재 확인할 목표 수열의 인덱스

# 핵심 알고리즘: 1부터 n까지 순서대로 스택에 push하면서 수열 만들기
for i in range(1, n + 1):
    # 1부터 n까지 순서대로 스택에 push
    stack.append(i)
    result.append('+')
    
    # 스택의 top이 목표 수열의 현재 원소와 같다면 계속 pop
    # 이 과정으로 목표 수열을 순서대로 만들어감
    while stack and stack[-1] == seq[cur]:
        stack.pop()
        result.append('-')
        cur += 1  # 다음 목표 원소로 이동

# 결과 출력: 스택이 비어있으면 성공, 아니면 불가능
if stack:
    # 스택에 원소가 남아있다면 목표 수열을 만들 수 없음
    print('NO')
else:
    # 모든 연산이 성공적으로 완료됨 - 연산 순서 출력
    for c in result:
        print(c)