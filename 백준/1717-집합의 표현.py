# 백준 1717 - 집합의 표현(https://www.acmicpc.net/problem/1717)
# 참고 링크 : https://www.youtube.com/watch?v=AMByrd53PHM
"""
분리집합의 개념이 뭔지 배우고 적용하며 풀어봤다
"""



import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

n, m = map(int, sys.stdin.readline().split())
parant = [i for i in range(n + 1)]          # parant 초기화 - 최초엔 0부터 n까지의 모든 애들의 부모가 자기자신인 상태
                                            # parant[a] = b라면 a의 부모가 b인 것임, 현재는 임의의 x에 대해 parant[x] = x인 상태

def getParant(x):         # x의 부모(가장 조상)를 리턴
    if parant[x] == x:    # x의 부모가 자기자신이라면 x를 그대로 리턴
        return x        
    parant[x] = getParant(parant[x])     # x의 부모가 자기자신이 아님 -> x의 부모를 제일 조상인(?) 애로
    return parant[x]                     # 결국은 x의 가장 조상인 애를 리턴 

def union(x, y):        # x가 속한 집합과 y가 속한 집합 합치기 - 가장 조상인 애들을 비교해 더 작은 쪽으로 합침
    x, y = getParant(x), getParant(y)
    if x != y:
        parant[x] = y
"""
    if x < y:           
        parant[y] = x
    elif x > y:         
        parant[x] = y  를 할 필요가 없는 이유
: 처음에 분리집합을 공부할 땐 작은 쪽으로 합쳐야 한다!고 배워서 이렇게 구현했지만,
생각해보니 어찌됐든 부모가 같기만 하면 같은 집합안에 있는 것이고
어떠한 두 집합을 합칠 때 뭘로하던 부모만 같게만 해준다면 같은 집합으로 합쳐진다.
여기서 부모를 같게 해줄 때 다른 집합의 부모와 겹치게 하면 안되지만(즉 부모를 아무거나 막 쓰면 안됨)
분리집합의 특성상 자기들 안에서만(x의 부모로 해주던가 y의 부모로 해주던가하면) 해주면 겹칠 일이 없음
"""

def hasSameParant(x, y):         # x, y가 같은 부모를 같는지 즉 같은 집합에 속해있는지
    x, y = getParant(x), getParant(y)
    if x == y:
        return "YES"
    else:
        return "NO"


for i in range(m):
    c = list(map(int, sys.stdin.readline().split()))
    if c[0] == 0:
        union(c[1], c[2])
    else:
        print(hasSameParant(c[1], c[2]))

