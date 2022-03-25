# n^2 보다 덜 걸리는 방법으로 풀기

def trapping_rain(buildings):
    # left_highest[x] : x번째 건물 왼쪽에서 가장 높은 건물의 높이
    # right_highest[x] : x번째 건물 오른쪽에서 가장 높은 건물의 높이
    left_highest = [0 for _ in range(len(buildings))]
    right_highest = [0 for _ in range(len(buildings))]

    end = len(buildings) - 1

    for i in range(1, len(buildings)):
        left_highest[i] = max(left_highest[i - 1], buildings[i - 1])
        right_highest[end - i] = max(right_highest[end - i + 1], 
                                    buildings[end - i + 1])
    
    answer = 0

    for i in range(1, end):
        # if buildings[i] < min(left_highest[i], right_highest[i]):
        #     answer += min(left_highest[i], right_highest[i]) - buildings[i]
        upper_bound = min(left_highest[i], right_highest[i])
        answer += max(0, upper_bound - buildings[i])
    
    return answer

    
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
