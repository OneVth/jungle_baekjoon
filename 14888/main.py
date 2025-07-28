import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(index, current_val):
    global max_val, min_val
    
    if index == n: 
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return

    if operators[0] > 0:
        operators[0] -= 1
        dfs(index + 1, current_val + nums[index])
        operators[0] += 1

    if operators[1] > 0:
        operators[1] -= 1
        dfs(index + 1, current_val - nums[index])
        operators[1] += 1

    if operators[2] > 0:
        operators[2] -= 1
        dfs(index + 1, current_val * nums[index])
        operators[2] += 1

    if operators[3] > 0:
        operators[3] -= 1
        dfs(index + 1, int(current_val / nums[index]))
        operators[3] += 1

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # add, sub, mul, div

max_val = -int(10**9)
min_val = int(10**9)
result = 0

dfs(1, nums[0])

print(max_val)
print(min_val)