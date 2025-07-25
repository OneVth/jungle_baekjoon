import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline


def preorder(root, left, right):
    if root == ".":
        return

    print(root, end="")
    preorder(left[root], left, right)
    preorder(right[root], left, right)


def inorder(root, left, right):
    if root == ".":
        return

    inorder(left[root], left, right)
    print(root, end="")
    inorder(right[root], left, right)


def postorder(root, left, right):
    if root == ".":
        return

    postorder(left[root], left, right)
    postorder(right[root], left, right)
    print(root, end="")


n = int(input())

left = dict()
right = dict()

for _ in range(n):
    target, l, r = input().split()
    left[target] = l
    right[target] = r

preorder("A", left, right)
print()
inorder("A", left, right)
print()
postorder("A", left, right)
