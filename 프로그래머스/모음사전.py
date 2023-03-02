def solution(word):
    dict = {
        'A': 'E',
        'E': 'I',
        'I': 'O',
        'O': 'U'
    }

    word = list(word)
    answer = 0
    now = []

    while now != word:
        answer += 1
        if len(now) < 5:
            now.append("A")
            continue
        while now[-1] == "U":
            now.pop()
        now[-1] = dict[now[-1]]

    return answer