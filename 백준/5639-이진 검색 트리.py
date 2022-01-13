# 5639 - 이진검색트리
# 전위순회 방식으로 주어지는 이진검색트리를
# 후위순회 방식으로 출력

# import sys
# sys.setrecursionlimit(10**9)

# input = sys.stdin.readline

# class Tree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#     # 왼쪽 서브트리 생성
#     def make_left_subtree(self, node):
#         self.left = node
#     # 오른쪽 서브트리 생성
#     def make_right_subtree(self, node):
#         self.right = node
# # 새 노드를 삽입하는 함수
# def insert_to_Tree(tree, value):
#     if tree.value < value:
#         if not tree.right:
#             new_node = Tree(value)
#             tree.make_right_subtree(new_node)
#         else:
#             insert_to_Tree(tree.right, value)
#     elif value < tree.value:
#         if not tree.left:
#             new_node = Tree(value)
#             tree.make_left_subtree(new_node)
#         else:
#             insert_to_Tree(tree.left, value)
# # 후위순회 함수
# def postorder_traversal(tree):
#     if tree.left:
#         postorder_traversal(tree.left)
#     if tree.right:
#         postorder_traversal(tree.right)
#     print(tree.value)

# root_node_value = int(input())

# binary_search_tree = Tree(root_node_value)

# while True:
#     try:
#         new_node_value = int(input())
#         insert_to_Tree(binary_search_tree, new_node_value)
#     except:
#         break
    
# postorder_traversal(binary_search_tree)

# 시간초과가 난다
# 생각해보니 트리에 특정 노드를 삽입하는 과정에서
# O(log n)이 아니라 O(n)이 걸릴 수도 있으므로
# 최악의 경우 O(n^2)만큼의 시간복잡도가 소요되고, n은 최대 10,000이므로
# 100,000,000번 정도 + 후위순회하는데 쓰이는 10,000번 정도의 연산을 하게 된다

# 어떻게 해결할 수 있을지 고민하다 인터넷을 참고..
# 전위순회한 걸 펼쳐서 보면
# 첫 출력 : 루트노드
# 그 뒤로 첫 출력보다 작은 애들 : 루트기준 왼쪽 서브트리의 노드들
# 그 뒤로 첫 출력보다 큰 애들 : 루트기준 오른쪽 서브트리의 노드들
# 임을 이용해 루트보다 큰 애들이 어디서부터 시작하는지만 알면
# 후위순회 순서대로 출력가능함을 이용

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

binary_search_tree = []

def post_order_print(left, right):
    if left > right:
        return
    else:
        middle = right + 1
        # 현재 구간에서 루트노드보다 큰 노드가 나오는 포인트 찾기
        for i in range(left + 1, right + 1):
            if binary_search_tree[i] > binary_search_tree[left]:
                middle = i
                break
        
        post_order_print(left + 1, middle - 1)
        post_order_print(middle, right)
        print(binary_search_tree[left])

while True:
    try:
        new_node = int(input())
        binary_search_tree.append(new_node)
    except:
        break

post_order_print(0, len(binary_search_tree) - 1)

# 의문인 점
# 10 9 8 7 6 5 4 3 2 1 와 같은 형태로 전위순회했다고 하면
# 자신보다 큰 값을 찾는 부분에서 항상 끝까지 루프를 돌아야 함
# 최악의 경우 이 역시도 O(n^2)정도의 연산을 할 것 같은데 왜 통과인지 모르겠다
