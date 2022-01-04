# 11725 - 트리의 부모 찾기
# 트리가 주어지고 루트노드를 1이라 할 때 2 ~ N번 노드의 부모 출력

# 1.무식하게 접근
# 입력 때마다 각 노드들에 연결된 노드들(부모 자식 상관X) 모두 표시
# 입력이 끝나면 1번은 어차피 루트라 부모가 없으므로 1번의 자식들의 연결노드에서 1번을 지우고,
# 걔네들의 자식들에 대해서도 같은 행동을 해주면 됨

import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

Tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    Tree[n1].append(n2)
    Tree[n2].append(n1)

answer = [0 for _ in range(N + 1)]

def mapping_parent(node, parent):
    for cnode in Tree[node]:
        if cnode != parent:
            answer[cnode] = node
            mapping_parent(cnode, node)

mapping_parent(1, 0)

for i in range(2, N + 1):
    print(answer[i])




