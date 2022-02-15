data = list(map(int, input().split()))

if data[0] == data[1] and data[1] == data[2]:
    print(10000 + data[0] * 1000)
elif data[0] == data[1]:
    print(1000 + data[0] * 100)
elif data[1] == data[2]:
    print(1000 + data[1] * 100)
elif data[0] == data[2]:
    print(1000 + data[0] * 100)
else:
    print(max(data) * 100)
