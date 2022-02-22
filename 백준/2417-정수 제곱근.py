N = int(input())

print(int(N ** 0.5) if (int(N ** 0.5)) ** 2 == N else int(N ** 0.5) + 1)