def solution(new_id):
    new_id = new_id.lower() #1
    
    temp = ""
    for ch in new_id:
        if ch.isdigit() or ch.isalpha() or ch in ['-', '_', '.']:
            temp += ch
    new_id = temp

    while new_id.count(".."): #3
        new_id = new_id.replace("..", ".")
    
    new_id = new_id.strip(".") #4
    
    new_id = "a" if not new_id else new_id #5
    
    if len(new_id) > 15: #6
        new_id = new_id[:15]
        new_id.rstrip(".")
    
    if len(new_id) < 3: #7
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    return new_id
    

print(solution("...!@BaT#*..y.abcdefghijklm"))