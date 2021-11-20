"""
무식하게 풀기 : 각 원소를 순회하며 쌍이 되는 조합 모조리 찾기
시간복잡도는 O(n^2)가 됨. n의 최대는 100만이므로 대략 1000억이 넘는 연산을 하게 됨
1초 내에 통과불가 ㅋㅋㅋㅋㅋ

투포인터를 통해 다루자.
"""
import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

target = int(sys.stdin.readline())

data.sort()

left, right, count = 0, len(data) - 1, 0

while left < right:
    if data[left] + data[right] == target:
        count += 1
        left += 1
        right -= 1
    elif data[left] + data[right] > target:
        right -= 1
    else:
        left += 1

print(count)