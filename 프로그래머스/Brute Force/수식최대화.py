# 100-200*300-500+20 이란 식이 있고, 연산자 우선순위를 * > + > - 라고 했다면
# 결국 - 연산을 마지막에 해야 함. 
# 따라서 위 식을 -를 기준으로 100, 200*300, 500+20 이렇게 쪼갰다면 쪼갠 식들을
# 전부 계산한 후, 그 결과들을 -연산해주면 된다.


from itertools import permutations

def calculate(exp, pr, index):
    # 가장 우선순위 낮은 애를 기준으로 식 쪼개기
    mid_exps = exp.split(pr[index])

    if index > 0:
        for i in range(len(mid_exps)):
            # 재귀를 통해 쪼갠 각각의 식들을 계산해준다
            mid_exps[i] = str(calculate(mid_exps[i], pr, index - 1))
    # 최종계산
    ret = eval(pr[index].join(mid_exps))

    return ret 

def solution(expression):
    answer = 0

    priorities = permutations(['*', '+', '-'], 3)

    for pr in priorities:
        answer = max(answer, abs(calculate(expression, pr, 2)))

    return answer
    


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
