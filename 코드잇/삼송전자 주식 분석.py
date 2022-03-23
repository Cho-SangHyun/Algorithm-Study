def max_profit(stock_list):
    buy = stock_list[0]
    answer = []
    for i in range(1, len(stock_list)):
        profit = stock_list[i] - buy
        answer.append(profit)
        buy = min(buy, stock_list[i])
    return max(answer)

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))