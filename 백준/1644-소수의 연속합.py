import math

N = int(input())

# num이하의 소수들 리스트로 반환
def get_primes(num):
    check = [True for i in range(num + 1)]

    for i in range(2, int(math.sqrt(num)) + 1):
        if check[i]:
            for j in range(i*2, num + 1, i):
                check[j] = False
    
    return [i for i in range(2, num + 1) if check[i] == True]

def solution(target):
    # 예외처리 : 1이면 0이 답이고 2면 1이 답임
    if target <= 2:
        return target - 1

    answer = 0
    primes = get_primes(target)
    left, right = 0, 1
    # prime_sum : left ~ right까지의 구간합
    prime_sum = primes[left] + primes[right]

    while left <= right and right < len(primes):
        if prime_sum == target:
            answer += 1
            left += 1
            prime_sum -= primes[left - 1]
        elif prime_sum < target: # 타겟이 더 큼 -> 합을 늘려야 함
            right += 1
            # 모듈러 연산을 통해 index Error 방지
            prime_sum += primes[right % len(primes)]
        else: # 타겟이 더 작음 -> 합을 줄여야 함
            left += 1
            prime_sum -= primes[left - 1]
    
    return answer

print(solution(N))