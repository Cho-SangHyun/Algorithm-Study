"""
모음과 자음을 따로 분리하고,
모음은 1개 이상, 자음은 2개 이상 골라 나오는 모든 조합을 본다
"""
from itertools import combinations
import sys

L, C = map(int, sys.stdin.readline().split())

# data[0] = 자음, data[1] = 모음
data = [list(map(str, sys.stdin.readline().split())), []]
password_list = []
# 자음 모음 분리 - 알파벳이 15개 주어지면 최대 75번 순회하므로 이 부분이 시간복잡도에 큰 영향을 주지 않으리라 생각했다.
for ch in ['a', 'e', 'i', 'o', 'u']:
    if ch in data[0]:
        data[1].append(ch)
        data[0].remove(ch)

# 주어진 알파벳들로 암호를 만들 수 있을 경우는 자음이 2개, 모음이 1개 이상인 경우
if len(data[0]) >= 2 and len(data[1]) >= 1: 

    # i는 모음의 개수를 의미
    for i in range(1, len(data[1]) + 1):
        if L - i >= 2:
            vowels = list(combinations(data[1], i)) # 가능한 모든 모음의 조합
            consos = list(combinations(data[0], L - i)) # 그로부터 생기는 가능한 모든 자음의 조합
            for v in vowels:
                for c in consos:
                    # 모음의 조합과 자음의 조합들을 합쳐 비밀번호만들기
                    password = ''.join(sorted(list(v + c)))
                    password_list.append(password)

    # 비밀번호들 사전순 정렬
    password_list.sort()

    for i in password_list:
        print(i)


"""
어림짐작을 해서 직관적으로 떠오른 방법(가능한 모든 경우를 조합해보기)가 시간 내에 될 수 있을지 판단해보고 싶었지만
다른 문제들과는 달리 어림짐작을 하는 게 힘들어서 코드를 짰는데 우연히 통과가 된 것 같다.

처음엔 24번줄이 없어서 30%쯤에서 틀렸습니다가 나왔다. 입력을 받은 시점에만 자음개수 >= 2, 모음개수 >= 1를 판단해주면
된다고 생각했는데 그게 아니었다. 입력받은 시점에서 판단하는 것은 비밀번호를 아예 만들 수 있냐 없냐를 따지는 거고, 
중간중간에도 내가 쓸려는 모음의 개수에 대해 자음의 개수가 조건에 만족되는지를 따져야 했다. 그래서 24번줄을 추가했다.

"""