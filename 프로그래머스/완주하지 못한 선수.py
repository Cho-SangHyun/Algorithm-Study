from collections import defaultdict

def solution(participant, completion):
    names = defaultdict(int)
    for n in completion:
        names[n] += 1
    
    for n in participant:
        if n in names and names[n] >= 1:
            names[n] -= 1
        else:
            return n
            
    

solution(["leo", "kiki", "eden"], ["eden", "kiki"])