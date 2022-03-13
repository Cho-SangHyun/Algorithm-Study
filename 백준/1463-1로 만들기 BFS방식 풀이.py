from collections import deque

N = int(input())
LIMIT_NUM = 10 ** 6

q = deque([(N, 0)])
calculated = set()

while q:
    value, count = q.popleft()
    
    if value == 1:
        print(count)
        exit(0)
    
    if value % 3 == 0 and value // 3 not in calculated:
        q.append((value // 3, count + 1))
        calculated.add(value // 3)
    if value % 2 == 0 and value // 2 not in calculated:
        q.append((value // 2, count + 1))
        calculated.add(value // 2)
    if (value - 1) not in calculated: 
        q.append((value - 1, count + 1))
        calculated.add(value - 1)
