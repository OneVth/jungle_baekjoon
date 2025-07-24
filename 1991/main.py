import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root: Node):
    if not root:
        return

    print(root.val, end="")
    preorder(root.left)
    preorder(root.right)


def inorder(root: Node):
    if not root:
        return

    inorder(root.left)
    print(root.val, end="")
    inorder(root.right)


def postorder(root: Node):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end="")


def search_node(root: Node, val) -> Node:
    if not root:
        return None

    if root.val == val:
        return root

    return search_node(root.left, val) or search_node(root.right, val)


n = int(input())

line = input().split()

root = Node(line[0])
for _ in range(n - 1):
    if line[1] != ".":
        ptr = search_node(root, line[0])
        if ptr:
            ptr.left = Node(line[1])

    if line[2] != ".":
        ptr = search_node(root, line[0])
        if ptr:
            ptr.right = Node(line[2])

    line = input().split()



preorder(root)
print()
inorder(root)
print()
postorder(root)
