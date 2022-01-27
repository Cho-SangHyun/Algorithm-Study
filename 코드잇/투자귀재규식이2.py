# 가장 부분합이 큰 구간 찾기, not Brute Force
# 분할정복으로 시도
# 구간을 반반 나워서 왼쪽에서 나오는 최대구간과 오른쪽에서 나오는 최대구간을 일단 구함.
# 좌에서 구한 start와 우에서 구한 end까지의 합이 왼쪽에서 나온 최대구간합과 우측의 최대구간 합보다 크다?
# 그러면 최대구간 = 좌start ~ 우end
# 만약 그렇지 않다면 좌에서 구한 최대구간합과 우에서 구한 최대구간합 중 더 큰 구간이 전체의 최대구간이 됨

def get_max_range(profits, start, end):
    if start == end:
        return (profits[start], start, end)

# start ~ end까지의 최대합 리턴하는 함수
def sublist_max(profits, start, end):
    if start == end:
        return (profits[start], start, end)

    mid = (start + end) // 2
    # left_max : 좌측 구간의 최대합, right_max : 우측 구간의 최대합
    left_max, left_start, left_end = sublist_max(profits, start, mid)
    right_max, right_start, right_end = sublist_max(profits, mid + 1, end)

    new = sum(profits[left_start:right_end + 1])
    if new >= left_max and new >= right_max:
        answer = new
        start, end = left_start, right_end
    else:
        answer, start, end = (left_max, left_start, left_end) if left_max > right_max else (right_max, right_start, right_end)

    
    return (answer, start, end)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1)[0])

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1)[0])

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1)[0])

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1)[0])
