import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def print_post(pre, start, end):
    if start > end:
        return
    
    root = pre[start]
    i = start + 1
    while i <= end and root > pre[i]:
        i += 1
    print_post(pre, start + 1, i - 1)
    print_post(pre, i, end)
    print(root)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

print_post(pre, 0, len(pre) - 1)