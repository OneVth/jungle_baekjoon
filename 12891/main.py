import sys

input = sys.stdin.readline

def check_valid(current_count, required):
    """현재 윈도우가 조건을 만족하는지 확인"""
    for i in range(4):
        if current_count[i] < required[i]:
            return False
    return True

s, p = map(int, input().split())
dna = input().strip()
required = list(map(int, input().split()))  # A, C, G, T 순서

# DNA 문자를 인덱스로 매핑
char_to_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

# 첫 번째 윈도우 초기화
current_count = [0, 0, 0, 0]
for i in range(p):
    char_idx = char_to_idx[dna[i]]
    current_count[char_idx] += 1

# 첫 번째 윈도우 검사
result = 0
if check_valid(current_count, required):
    result += 1

# 슬라이딩 윈도우
for i in range(s - p):
    # 왼쪽 문자 제거
    left_char_idx = char_to_idx[dna[i]]
    current_count[left_char_idx] -= 1
    
    # 오른쪽 문자 추가
    right_char_idx = char_to_idx[dna[i + p]]
    current_count[right_char_idx] += 1
    
    # 조건 확인
    if check_valid(current_count, required):
        result += 1

print(result)
