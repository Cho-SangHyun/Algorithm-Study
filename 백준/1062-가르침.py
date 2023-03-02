from itertools import combinations
import sys
input = sys.stdin.readline


def solution(n, k, words):
    if k < 5:
        return 0

    total_alphas = set()
    basic = set(['a', 'n', 't', 'i', 'c'])
    alphas_per_word = []

    for word in words:
        alphas = set()
        for ch in word[4:-4]:
            if ch in basic:
                continue
            alphas.add(ch)
            total_alphas.add(ch)
        alphas_per_word.append(alphas)

    answer = -1

    x = k - 5 if len(total_alphas) >= k - 5 else len(total_alphas)

    for comb in combinations(total_alphas, x):
        comb = set(comb)
        mid_answer = 0
        for alpha in alphas_per_word:
            if len(alpha) == 0:
                mid_answer += 1
                continue
            for ch in alpha:
                if ch not in comb:
                    break
            else:
                mid_answer += 1
        answer = max(answer, mid_answer)
    return answer


N, K = map(int, input().split())
_words = [input().strip() for _ in range(N)]

print(solution(N, K, _words))
