def get_distance(pos1, pos2):
        r_dis = abs(pos1[0] - pos2[0])
        c_dis = abs(pos1[1] - pos2[1])
        return r_dis + c_dis

def solution(numbers, hand):
    answer = ''
    
    num_pad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }

    left_pos = [3, 0]
    right_pos = [3, 2]

    for num in numbers:
        if num in set([1, 4, 7]):
            answer += 'L'
            left_pos = num_pad[num]
        elif num in set([3, 6, 9]):
            answer += 'R'
            right_pos = num_pad[num]
        else:
            left_distance, right_distance = get_distance(num_pad[num], left_pos), get_distance(num_pad[num], right_pos)
            if left_distance < right_distance:
                answer += 'L'
                left_pos = num_pad[num]
            elif left_distance > right_distance:
                answer += 'R'
                right_pos = num_pad[num]
            elif hand == "left":
                answer += 'L'
                left_pos = num_pad[num]
            else:
                answer += 'R'
                right_pos = num_pad[num]

    return answer