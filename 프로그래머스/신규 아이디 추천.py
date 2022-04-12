def solution(new_id):
    # can_ch = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.'])
    can_ch = set(['-', '_', '.'])
    new_id = new_id.lower()
    answer = ''
    for ch in new_id:
        # if ch in can_ch or (ch >= 'a' and ch <= 'z'):
        if ch.isalnum() or ch in can_ch:
            answer += ch
    while ".." in answer:
        answer = answer.replace("..", ".")
    answer = answer.strip(".")

    if len(answer) == 0:
        answer = "a"
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    while len(answer) <= 2:
        answer += answer[-1]
    return answer
