import sys
from itertools import combinations

input = sys.stdin.readline

def calculate_team_score(team, mat):
    """팀의 능력치를 계산하는 함수"""
    score = 0
    for i in team:
        for j in team:
            if i != j:
                score += mat[i][j]
    return score

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

people = list(range(n))
min_diff = float('inf')

# N/2명을 선택하는 모든 조합을 확인
for start_team in combinations(people, n // 2):
    # 스타트 팀에 속하지 않은 사람들이 링크 팀
    link_team = [p for p in people if p not in start_team]
    
    # 각 팀의 능력치 계산
    start_score = calculate_team_score(start_team, mat)
    link_score = calculate_team_score(link_team, mat)
    
    # 능력치 차이 계산 및 최솟값 갱신
    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)
    

print(min_diff)