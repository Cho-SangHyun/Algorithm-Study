N = int(input())

mock, namuzi = N // 3, N % 3

if not namuzi:
    if mock % 2 == 0:
        print("CY")
    else:
        print("SK")
else:
    if (mock % 2 == 0 and namuzi == 1) or (mock % 2 == 1 and namuzi == 2):
        print("SK")
    else:
        print("CY")