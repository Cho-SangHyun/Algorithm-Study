import sys
sys.setrecursionlimit(10**9)

from collections import defaultdict

def dfs(visited_path, min_intensity, intensity, time, prev_point, point, summit):
    prev_intensity = intensity

    if not visited_path[prev_point][point]:
        if point == summit:
            min_intensity = min(min_intensity, intensity)
            return

        visited_path[prev_point][point] = 1
        visited_path[point][prev_point] = 1

        for next_point in time[point]:
            intensity = max(intensity, time[point][next_point])
            dfs(visited_path, min_intensity, intensity, time, point, next_point, summit)

        visited_path[prev_point][point] = 0
        visited_path[point][prev_point] = 0      

    intensity = prev_intensity

def getMinimunIntensity(point_num, time, gate, summit):
    visited_path = [[0 for _ in range(point_num + 1)] for _ in range(point_num + 1)]
    # gate에서 summit으로 가는 경로 중 가장 작은 intensity
    min_intensity = 123456789
    intensity = -1
    for next_point in time[gate]:
        intensity = max(intensity, time[gate][next_point])
        dfs(visited_path, min_intensity, intensity, time, gate, next_point, summit)
    

    return min_intensity

def solution(n, paths, gates, summits):
    time = [defaultdict() for _ in range(n + 1)]

    for path in paths:
        p1, p2, t = path
        time[p1][p2] = t
        time[p2][p1] = t

    answer_summit, answer_intensity = 123456789, 123456789
    
    for gate in gates:
        for summit in summits:
            going_intensity = getMinimunIntensity(n, time, gate, summit)
            back_intensity = getMinimunIntensity(n, time, summit, gate)
            intensity = max(going_intensity, back_intensity)
            if intensity < answer_intensity:
                answer_intensity = intensity
                answer_summit = summit
            elif intensity == answer_intensity:
                answer_summit = min(answer_summit, summit)
    
    return [answer_summit, answer_intensity]

print(solution(
    6, 
    [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], 
    [1, 3], 
    [5]
    ))

print(solution(
    7, 
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], 
    [3, 7], 
    [1, 5]
    ))