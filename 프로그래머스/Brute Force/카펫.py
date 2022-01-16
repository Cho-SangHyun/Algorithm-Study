# from sqlite3 import Row


# 백준 고득점 Kit 완전탐색 - 카펫문제
# 갈색타일 수와 노란색 타일 수가 주어졌을 때 전체 타일 배치의
# row, col 출력하기
# 갈색타일 수 최대 5,000, 노란타일 수 최대 2,000,000
# col이 row보다 크거나 같아야 한다

# 전체타일 수 = 갈색타일 + 노란타일 즉 최댜 2,005,000
# row의 최소 = 3부터 시작해야 함.
# row를 3부터 시작해 하나하나 늘려가며 row * col = 전체타일 수가 되는 row가
# 있는지 찾고, 있으면 테두리 1줄이 갈색, 내부가 노란색타일로 채웠을 때 일치하는지 판단하기
# 러프하게 생각해도 최대 200만번 정도만 수행

def solution(brown, yellow):
    entire_tile = brown + yellow

    row, col = 3, 3

    answer = []

    while True:
        if entire_tile % row == 0:
            col = entire_tile // row
            if row > col:
                break
            brown_tile = 2 * col + 2 * (row - 2)
            yellow_tile = entire_tile - brown_tile
            if brown_tile == brown and yellow_tile == yellow:
                answer = [col, row]
        row += 1

    return answer

