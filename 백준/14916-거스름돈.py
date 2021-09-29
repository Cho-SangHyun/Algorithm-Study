n = int(input())

if n == 1 or n == 3:                  # n이 1 or 3 : 거스름돈 못준다 
    print(-1)
else:
    coin = 0
    if n % 5 == 1 or n % 5 == 3:      # 5로 나눈 나머지가 홀수 : n을 5로 나눈 몫 - 1 + 나머지에 5를 더한 값을 2로 나눈 몫이 답
        coin += ((n // 5) - 1)
        coin += ((n % 5) + 5) // 2
    else:                             # 5로 나눈 나머지가 짝수 : n을 5로 나눈 몫 + 나머지를 2로 나눈 몫이 답
        coin += n // 5
        coin += (n % 5) // 2
    print(coin)