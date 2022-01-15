# 2250 - 트리의 높이와 너비
# 이진트리가 주어질 때, 가장 너비가 넓은 레벨과 그 너비를 출력
# 노드 수는 1이상 10,000이하

# 1. 트리를 리스트 형태로 입력받고, 루트노드를 찾은 후(DFS로)
# 2. 트리의 노드별로 왼쪽 서브트리와 오른쪽 서브트리의 노드개수를 파악(재귀로)
# 3. 트리의 각 레벨 별 끝 노드들을 파악 후(BFS로)
# 4. 2에서 한 것을 토대로 각 노드들의 열 위치를 정할 수 있음
# 5. 다 정해지면, 3에서 구한 레벨 별 끝 노드들의 열 위치들을 이용해 너비를 파악가능

# 이진트리의 간선 개수 = N - 1개이므로
# DFS, BFS돌 때 시간복잡도 = 러프하게 O(2N)정도
# 재귀로 노드의 왼쪽 서브/오른쪽 서브트리 노드개수를 파악하는 것은
# 노드개수만큼의 재귀함수를 호출하므로 O(N)정도
# 각 노드들의 열 위치 정하는 것도 노드개수만큼의 재귀를 호출하므로 O(N)정도
# 전체시간복잡도는 O(N)정도가 될 것이라 예상해서 시간 내에 통과 가능하리라 생각함

import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())
# Tree[x][0] : x의 부모, [x][1] : x의 left, [x][2] : x의 right
# 0인 값은 없다는 것을 의미하도록 함(ex : Tree[x][1]이 0이면 x는 왼쪽 노드가 안 달려있다)
Tree = [[0, 0, 0] for _ in range(N + 1)]
# 트리 입력받기
for _ in range(N):
    node, left, right = map(int, input().split())
    if left != -1:
        Tree[node][1] = left
        Tree[left][0] = node
    if right != -1:
        Tree[node][2] = right
        Tree[right][0] = node
# 루트노드 찾기 - DFS로(BFS보단 DFS가 구현이 더 쉽다고 생각해 DFS로 구현)
visited = {0}
stack, root = [1], 0

while stack:
    node = stack.pop()
    if node and node not in visited:
        # 현재 순회중인 노드가 부모 노드가 없다? 루트노드다
        if not Tree[node][0]:
            root = node
            break
        visited[node] = True
        stack += list(set(Tree[node]) - set(visited))

# x를 루트로 하는 트리의 왼쪽 서브트리 수, 오른쪽 서브트리 수를 기록하고 전체 노드 수를 리턴하는 함수 선언
def get_num_of_node(x):
    if x == 0:
        return 0
    left_subtree_count = get_num_of_node(Tree[x][1])
    right_subtree_count = get_num_of_node(Tree[x][2])
    Tree[x].append(left_subtree_count)
    Tree[x].append(right_subtree_count)
    # Tree[x][3], Tree[x][4] = left_subtree_count, right_subtree_count
    # 전체 노드수 : 자기 자신(루트노드) 1개 + 왼쪽 서브트리 노드수 + 오른쪽 서브트리 노드수
    return 1 + left_subtree_count + right_subtree_count
# 선언한 함수를 이용해 트리의 각 노드들에개 왼쪽 서브노드 수, 오른쪽 서브트리 노드수를 기록
get_num_of_node(root)
# 레벨별 끝 노드들을 저장할 배열
# ex) level[x][0] : x레벨의 왼쪽 끝노드, level[x][1] : x레벨의 오른쪽 끝노드 이런식
level = [0 for _ in range(N + 1)]

visited = {}
queue, level_idx = deque([[root]]), 1
# BFS를 통해 레벨별 끝 노드들 저장하기
while queue:
    nodes = queue.popleft()
    # 큐에서 꺼낸 리스트에서 첫 노드 = 그 레벨의 왼쪽 끝노드, 마지막 노드 = 그 레벨의 마지막 노드
    level[level_idx] = [nodes[0], nodes[-1]]
    next_level_nodes = []
    for node in nodes:
        if Tree[node][1]:
            next_level_nodes.append(Tree[node][1])
        if Tree[node][2]:
            next_level_nodes.append(Tree[node][2])
    
    if next_level_nodes:
        # 같은 레벨의 노드들을 한꺼번에 리스트에 담겨진 형태 그대로 큐에 넣어줌
        # 이래야 그 레벨에서 왼쪽 끝, 오른쪽 끝노드가 뭔지 쉽게 파악 가능
        queue += [next_level_nodes]
    level_idx += 1
# 노드들의 위치할 열 값을 저장할 리스트 ex) node_column[x] = y -> 노드 x는 y번 열에 위치한다
node_column = [0 for _ in range(N + 1)]
# 각 노드들의 위치를 기록하는 함수
def func(left, right, node):
    if left > right:
        return
    x = left + Tree[node][3]
    node_column[node] = x
    func(left, x - 1, Tree[node][1])
    func(x + 1, right, Tree[node][2])

func(1, N, root)

answer_width = 0
answer_level = 0

for i in range(1, level_idx):
    now_width = abs(node_column[level[i][1]] - node_column[level[i][0]]) + 1
    if now_width > answer_width:
        answer_width = now_width
        answer_level = i

print(answer_level, answer_width)
