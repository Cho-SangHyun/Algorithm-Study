N = int(input())

string = input()

blue, red, i = 0, 0, 0

while i < N:
    if string[i] == 'B':
        i += 1
        while i < N and string[i] == 'B':
            i += 1
        blue += 1
    else:
        i += 1
        while i < N and string[i] == 'R':
            i += 1
        red += 1

print(1 + min(blue, red))



