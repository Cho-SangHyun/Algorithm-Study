N = int(input())

answer = 0

for i in range(1, N + 1):
    answer += i * (N // i)

print(answer)

# 특정 수의 약수 찾기
# 1부터 N까지 탐색하며 나누어떨어지는지 조사
# 1부터 N의 절반까지 탐색하며 나누어떨어지는지 조사
# 1부터 logN까지 탐색하며 나누어떨어지는지 조사

# But N보다 같거나 작은 수들 중 1의 배수, 그러니까 1을 약수로 갖는 애들의 수 = N // 1개
# N보다 같거나 작은 수들 중 2의 배수, 그러니까 2를 약수로 갖는 애들의 수 = N // 2개
# N보다 같거나 작은 수들 중 3의 배수, 그러니까 3을 약수로 갖는 애들의 수 = N // 3개

# 이 논리로 풀 수 있다.
