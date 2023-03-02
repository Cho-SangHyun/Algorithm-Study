def is_crossed(x_line, y_line):
    if x_line[0] < y_line[0] < x_line[2] and y_line[1] < x_line[1] < y_line[3]:
        return True
    return False


def is_override(x_line, y_line):
    if x_line[0] <= y_line[0] <= x_line[2] and y_line[1] <= x_line[1] <= y_line[3]:
        return True
    return False


def solution(lines):
    x_lines, y_lines = [[] for _ in range(101)], [[] for _ in range(101)]
    for line in lines:
        if line[0] == line[2]:
            y_lines[line[0]].append(line)
        else:
            x_lines[line[1]].append(line)

    final_x_lines, final_y_lines = [], []

    for i in range(101):
        x_lines[i].sort(key=lambda x: x[0])
        y_lines[i].sort(key=lambda x: x[1])

    for x_line in x_lines:
        if not x_line:
            continue
        if len(x_line) == 1:
            final_x_lines.append(x_line[0])
            continue
        s, e = x_line[0][0], x_line[0][2]
        for i in range(1, len(x_line)):
            if x_line[i][0] <= e:
                e = max(e, x_line[i][2])
            else:
                final_x_lines.append([s, x_line[0][1], e, x_line[0][1]])
                s, e = x_line[i][0], x_line[i][2]
        final_x_lines.append([s, x_line[0][1], e, x_line[0][1]])

    for y_line in y_lines:
        if not y_line:
            continue
        if len(y_line) == 1:
            final_y_lines.append(y_line[0])
            continue
        s, e = y_line[0][1], y_line[0][3]
        for i in range(1, len(y_line)):
            if y_line[i][1] <= e:
                e = max(e, y_line[i][3])
            else:
                final_y_lines.append([y_line[0][0], s, y_line[0][0], e])
                s, e = y_line[i][1], y_line[i][3]
        final_y_lines.append([y_line[0][0], s, y_line[0][0], e])

    answer = 0

    for i in range(len(final_x_lines)):
        for j in range(len(final_y_lines)):
            x_line = final_x_lines[i]
            y_line = final_y_lines[j]

            if is_crossed(x_line, y_line):
                cross_x, cross_y = y_line[0], x_line[1]
                upper_length = abs(y_line[3] - cross_y)
                right_length = abs(x_line[2] - cross_x)
                left_length = abs(x_line[0] - cross_x)
                lower_length = abs(y_line[1] - cross_y)

                if i != len(final_x_lines) - 1 and is_override(final_x_lines[i + 1], y_line):
                    upper_length = min(upper_length, abs(final_x_lines[i + 1][1] - cross_y))

                if i != 0 and is_override(final_x_lines[i - 1], y_line):
                    lower_length = min(lower_length, abs(final_x_lines[i - 1][1] - cross_y))

                if j != len(final_y_lines) - 1 and is_override(x_line, final_y_lines[j + 1]):
                    right_length = min(right_length, abs(final_y_lines[j + 1][0] - cross_x))

                if j != 0 and is_override(x_line, final_y_lines[j - 1]):
                    left_length = min(left_length, abs(final_y_lines[i - 1][0] - cross_x))

                answer = max(answer, min(upper_length, right_length, left_length, lower_length))

    return answer


print(solution([
    [1, 4, 5, 4],
    [2, 3, 2, 7],
    [5, 4, 8, 4],
    [2, 6, 3, 6],
    [3, 2, 7, 2],
    [6, 1, 6, 7],
    [3, 5, 3, 8],
    [3, 2, 3, 6]
]))
