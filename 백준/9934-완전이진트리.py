import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

nodes_per_level = [[] for _ in range(N + 1)]



def insert_node(st, ed, level):
    if st > ed:
        return
    
    mid = (st + ed) // 2

    nodes_per_level[level].append(data[mid])

    insert_node(st, mid - 1, level + 1)
    insert_node(mid + 1, ed, level + 1)



insert_node(0, len(data) - 1, 1)

for lv in range(1, N + 1):
    print(' '.join(map(str, nodes_per_level[lv])))
