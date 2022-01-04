import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())

Tree = {}

for _ in range(N):
    node, left, right = input().split()
    Tree[node] = [left, right]

def preorder_traversal(node):
    left_node = Tree[node][0]
    right_node = Tree[node][1]

    print(node, end='')
    if left_node != '.':
        preorder_traversal(left_node)
    if right_node != '.':
        preorder_traversal(right_node)

def inorder_traversal(node):
    left_node = Tree[node][0]
    right_node = Tree[node][1]

    if left_node != '.':
        inorder_traversal(left_node)
    print(node, end='')
    if right_node != '.':
        inorder_traversal(right_node)

def postorder_traversal(node):
    left_node = Tree[node][0]
    right_node = Tree[node][1]

    if left_node != '.':
        postorder_traversal(left_node)
    if right_node != '.':
        postorder_traversal(right_node)
    print(node, end='')


preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')