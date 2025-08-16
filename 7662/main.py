# BOJ 7662 - 이중 우선순위 큐
# 알고리즘: 두 개의 힙 + 유효성 추적
# 시간복잡도: O(k log k) (k는 연산의 개수)

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

# 입력 처리: 테스트 케이스의 개수
t = int(input())

for _ in range(t):
    # 각 테스트 케이스별 연산 개수 입력
    n = int(input())
    
    # 데이터 구조 초기화
    max_heap = []                    # 최댓값 추출용 힙 (음수로 저장하여 max heap 구현)
    min_heap = []                    # 최솟값 추출용 힙
    count = defaultdict(int)         # 각 값의 유효한 개수 추적 (lazy deletion용)

    # 핵심 알고리즘: 각 연산 처리
    for _ in range(n):
        operation, value = input().split()
        value = int(value)

        if operation == "I":
            # 삽입 연산: 양쪽 힙에 모두 추가하고 카운트 증가
            heapq.heappush(max_heap, -value)  # 음수로 저장하여 최댓값 추출 가능
            heapq.heappush(min_heap, value)
            count[value] += 1
        else:
            # 삭제 연산: 큐에 원소가 있을 때만 실행
            if count:  # count 딕셔너리에 유효한 원소가 있는지 확인
                if value == -1:
                    # 최솟값 삭제
                    # lazy deletion: 유효하지 않은 원소들을 먼저 제거
                    while min_heap and count[min_heap[0]] == 0:
                        heapq.heappop(min_heap)
                    # 유효한 최솟값이 있다면 삭제
                    if min_heap:
                        min_val = heapq.heappop(min_heap)
                        count[min_val] -= 1
                else:
                    # 최댓값 삭제 (value == 1)
                    # lazy deletion: 유효하지 않은 원소들을 먼저 제거
                    while max_heap and count[-max_heap[0]] == 0:
                        heapq.heappop(max_heap)
                    # 유효한 최댓값이 있다면 삭제
                    if max_heap:
                        max_val = -heapq.heappop(max_heap)  # 음수를 다시 양수로 변환
                        count[max_val] -= 1

    # 최종 결과 출력 전 정리: 유효하지 않은 원소들 제거
    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    # 결과 출력: 최댓값과 최솟값 또는 EMPTY
    if min_heap and max_heap:
        # 둘 다 비어있지 않으면 최댓값과 최솟값 출력
        print(-max_heap[0], min_heap[0])
    else:
        # 큐가 비어있으면 EMPTY 출력
        print("EMPTY")
