def solution(lottos, win_nums):
    win_nums = set(win_nums)
    
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt, zero_cnt = 0, 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        elif num in win_nums:
            cnt += 1
    
    min_value = 1 if zero_cnt == 6 else cnt
    max_value = cnt + zero_cnt
    
    answer = [rank[max_value], rank[min_value]]
    
    return answer