import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def postorder(preorder_list, start, end):
    if start > end:
        return
    
    root = preorder_list[start]
    i = start + 1
    while i <= end and preorder_list[i] < root:
        i += 1

    postorder(preorder_list, start + 1, i - 1)
    postorder(preorder_list, i, end)
    print(root)

preorder_list = []
while True:
    try:
        preorder_list.append(int(input()))
    except:
        break

postorder(preorder_list, 0, len(preorder_list) - 1)