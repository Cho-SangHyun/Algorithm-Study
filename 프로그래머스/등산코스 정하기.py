import heapq


def solution(n, paths, gates, summits):
    summits.sort()
    gates_set = set(gates)
    answer_intensity = 987654321
    answer_summit = -1

    graph = [[] for _ in range(n + 1)]
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))

    for start in gates:
        for goal in summits:
            summits_set = set(summits) - set([goal])
            intensities = [987654321 for _ in range(n + 1)]
            intensities[start] = 0
            q = []
            heapq.heappush(q, (0, start))

            while q:
                intensity, now = heapq.heappop(q)
                if intensities[now] < intensity:
                    continue
                for child, cost in graph[now]:
                    if child in gates_set or child in summits_set:
                        continue
                    new_intensity = max(cost, intensity)
                    if new_intensity < intensities[child]:
                        intensities[child] = new_intensity
                        heapq.heappush(q, (new_intensity, child))

            if intensities[goal] < answer_intensity:
                answer_intensity = intensities[goal]
                answer_summit = goal

    return [answer_summit, answer_intensity]