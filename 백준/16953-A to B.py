"""
무식하게 풀기: 할 수 있는 연산은
1) x2
2) x10 and +1
밖에 없으므로 만들어야 할 값이 짝수거나 끝이 1로 끝나는 수가 아니면 애당초 만들 수 없음

1) B가 짝수면 나누기2
2) B의 끝이 1이면 10으로 나눈 몫
을 반복해서 해주면서 B가 A랑 같아지면 count한 값이 정답이고
B가 A보다 작아지면 불가능, B가 1, 2에 해당하지 않는 수가 되면 불가능

A는 최소1, B는 최대 10^9이 주어지면 
약 log10^9 = 27번? 정도의 연산을 할 듯 하다 -> 2초 내에 통과 가능

"""

A, B = map(int, input().split())

count = 1

while A != B:
    if A > B : 
        count = -1
        break
    if B % 2 == 0: 
        count += 1
        B //= 2
    elif B % 10 == 1:
        count += 1
        B //= 10
    else:
        count = -1
        break

print(count)
