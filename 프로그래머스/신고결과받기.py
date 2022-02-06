# 신고한 유저에게 메일 발송
# 각 아이디별로 몇 개의 메일을 받는가?

from collections import defaultdict

def solution(id_list, report, k):
    answer, id_number = [], {}

    for i, id in enumerate(id_list):
        id_number[id] = i
        answer.append(0)
    
    report_graph = defaultdict(set)
    
    for rp in report:
        userID, reportID = rp.split()
        report_graph[reportID].add(userID)
    
    for id in id_list:
        if len(report_graph[id]) >= k:
            for r_id in report_graph[id]:
                answer[id_number[r_id]] += 1
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
