import sys

input = sys.stdin.readline

C = int(input())

def get_reverse_quad_tree(quad_tree):
    if quad_tree[0] == 'w' or quad_tree[0] == 'b':
        return quad_tree[0]
    else:
        section = ['', '', '', '', '']

        now, i = 1, 1

        while i < len(quad_tree):
            if quad_tree[i] == 'b' or quad_tree[i] == 'w':
                section[now] = quad_tree[i]
                now += 1
                i += 1
            # quad_tree[i] == 'x'
            else:
                # start ~ last까지가 그 영역의 압축 문자열
                start, last = i, i + 4
                i += 1

                while i <= last:
                    # x가 나오면 압축 문자열의 길이가 4씩 늘어난다.
                    if quad_tree[i] == 'x':
                        last += 4
                    i += 1
                
                section[now] = quad_tree[start:last+1]
                now += 1
        
        return (
            'x' + 
            get_reverse_quad_tree(section[3]) + 
            get_reverse_quad_tree(section[4]) + 
            get_reverse_quad_tree(section[1]) + 
            get_reverse_quad_tree(section[2])
        )


for _ in range(C):
    quad_tree = input().strip()
    print(get_reverse_quad_tree(quad_tree))

