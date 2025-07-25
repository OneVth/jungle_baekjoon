import sys

sys.setrecursionlimit(10**8)

class Node:

    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None

class Tree:

    def __init__(self, root: Node):
        self._root = root

    def search_node(self, node: Node, key) -> Node:
        """
        key를 기준으로 노드를 찾고 성공하면 Node를, 실패하면 None을 반환하는 함수입니다.
        """

        if not node:
            return None
        
        if node._key == key:
            return node
        
        return self.search_node(node._left, key) or self.search_node(node._right, key)
    
    def search_tree(self, key) -> Node:
        return self.search_node(self._root, key)
    
    def inorder(self, node: Node):
        if not node:
            return
        
        self.inorder(node._left)
        print(node._key, end='')
        self.inorder(node._right)

    def preorder(self, node: Node):
        if not node:
            return
        
        print(node._key, end='')
        self.preorder(node._left)
        self.preorder(node._right)

    def postorder(self, node: Node):
        if not node:
            return
        
        self.postorder(node._left)
        self.postorder(node._right)
        print(node._key, end='')

    def print_tree(self):
        self.inorder(self._root)

input = sys.stdin.readline

n = int(input())

target, left, right = input().split()

tree = Tree(Node(target))

ptr = tree._root
for i in range(n - 1):
    if ptr:
        ptr._left = Node(left) if left != '.' else None
        ptr._right = Node(right) if right != '.' else None
        
    
    target, left, right = input().split()
    ptr = tree.search_tree(target)

tree.preorder(tree._root)
print()
tree.inorder(tree._root)
print()
tree.postorder(tree._root)