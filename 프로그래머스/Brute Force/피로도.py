answer = 0


def dfs(k, dungeons, traveled):
    global answer
    answer = max(answer, len(traveled))

    for i in range(len(dungeons)):
        if i not in traveled and k >= dungeons[i][0]:
            traveled.add(i)
            dfs(k - dungeons[i][1], dungeons, traveled)
            traveled.remove(i)


def solution(k, dungeons):
    global answer

    traveled = set()
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            traveled.add(i)
            dfs(k - dungeons[i][1], dungeons, traveled)
            traveled.remove(i)

    return answer